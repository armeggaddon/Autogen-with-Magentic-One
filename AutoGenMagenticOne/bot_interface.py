import logging
import traceback
import gradio as gr
from magentic_one import get_tc_manager
from semantic_kernel.contents import ChatHistory

chat_history = ChatHistory()
logger = logging.getLogger(__name__)

async def test_case_agent(chat_history):
    
    organiser = get_tc_manager()
    
    async for content in organiser.invoke(chat_history):
        # Add the response to the chat history
        chat_history.add_message(content)
    ############################################################################################
    output_ = content.content     
    return output_


async def ag_magentic_one_invoker(user_message,history,session_id):
    
    try:

        chat_history.add_user_message(user_message)
        output_ = await test_case_agent(chat_history)
                  
        return output_    

    except Exception as e: 
        print(traceback.format_exc())
        logger.exception("######################### Error Processing the request in GPT model ############################")        
        output_ = "Error"


id_component = gr.State(value = 'AutoGenMagenticOne')
mo_demo = gr.ChatInterface(ag_magentic_one_invoker,
                        additional_inputs = [id_component],
                        chatbot=gr.Chatbot(label='Play with your queries!!!',
                                           avatar_images=('./images/user.png','./images/bot.png'),
                                           scale=1,
                                           height=400,
                                           type="messages",
                                           ),
                        title='Autogen - Magentic One Demo',
                        textbox=gr.Textbox(placeholder="Type your queries here", container=False, scale=7,submit_btn=True),
                        type="messages"
                                             
                        )

mo_demo.launch(share=True,server_port=int(8009))


