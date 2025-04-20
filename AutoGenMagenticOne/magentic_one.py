from typing import Annotated
from semantic_kernel import Kernel
from semantic_kernel.functions import kernel_function
from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.functions.kernel_arguments import KernelArguments
from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior

from autogen_agentchat.ui import Console
from autogen_ext.teams.magentic_one import MagenticOne
from autogen_ext.models.openai import AzureOpenAIChatCompletionClient
from constants import MODEL, AZURE_DEPLOYMENT, AZURE_ENDPOINT, API_VERSION, API_KEY


model_client = AzureOpenAIChatCompletionClient(model=MODEL,
                                               azure_deployment=AZURE_DEPLOYMENT,
                                               azure_endpoint=AZURE_ENDPOINT,
                                               api_version=API_VERSION,
                                               api_key=API_KEY)


def _create_kernel_with_chat_completion(service_id: str) -> Kernel:
    kernel = Kernel()

    kernel.add_service(
        AzureChatCompletion(
            service_id=service_id,
            deployment_name=AZURE_DEPLOYMENT,
            endpoint=AZURE_ENDPOINT,
            api_key=API_KEY,
            api_version=API_VERSION
        ),
    )        
    return kernel


def get_tc_manager():

    ORGANISER_NAME = "Co-Ordinator"
    ORGANISER_INSTRUCTIONS = """
        
        As a Coordinator, you need to interact with user and respond to their queries
        1. When user ask for a specific task to be accomplished you need to invoke AutoGenPlugin
        2. Once the plugin generates the response, summarize them and share with user
        
        """
        
    service_id = "tc_organiser"
    organiser_kernel = _create_kernel_with_chat_completion(service_id)
    
    organiser_kernel.add_plugin(AutoGenPlugin(), plugin_name="TaskAgent")
    settings = organiser_kernel.get_prompt_execution_settings_from_service_id(service_id=service_id)
    settings.function_choice_behavior = FunctionChoiceBehavior.Auto()
    
    agent_tc_organiser = ChatCompletionAgent(
        service_id=service_id,
        kernel=organiser_kernel,
        name=ORGANISER_NAME,
        instructions=ORGANISER_INSTRUCTIONS,
        arguments=KernelArguments(settings=settings),
    )
    return agent_tc_organiser


class AutoGenPlugin:
    """A AutoGenPlugin used to call task agent Magentic One"""

    @kernel_function(description="Takes the user action item and provide the final magentic one results")
    async def invoke_group_chat(self, user_action_item) -> Annotated[str, "Returns the final output to user"]:
        print("plugin::Invoked Autogen Magentic One")
        print(user_action_item)
        try:
            user_input = user_action_item.get('task')
        except AttributeError:
            user_input = user_action_item

        m1 = MagenticOne(client=model_client)
        result = await Console(m1.run_stream(task=user_input))
        
        full_length = len(result.messages)
        final_output_from_mo = result.messages[full_length - 1].content
        return final_output_from_mo