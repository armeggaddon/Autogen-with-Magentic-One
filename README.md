  
# 🌟 Autogen-MagenticOne (AGMO) for Open-Ended Tasks  
   
Welcome to the **Autogen-MagenticOne (AGMO)** repository! 🚀    
This project showcases **MagenticOne's** multiagent features to solve complex problems across a variety of domains.  
   
---  
   
## 📋 Table of Contents  
   
- [🌟 Project Overview](#-project-overview)  
- [🛠️ Pre-requisites](#%EF%B8%8F-pre-requisites)  
- [📖 Introduction to AGMO](#-introduction-to-agmo)  
- [🧩 Components of MagenticOne](#-components-of-magenticone)  
- [💻 Example Code](#-example-code)  
- [⚠️ Important Notes](#-important-notes)  
- [📜 License](#-license)  
   
---  
   
## 🌟 Project Overview  
   
Autogen-MagenticOne (AGMO) is a **multiagent system** designed to resolve open-ended tasks. It leverages cutting-edge tools such as `SemanticKernel`, `Gradio`, and `Azure OpenAI` to create an advanced architecture for agent-based problem-solving.  
   
---  
   
## 🛠️ Pre-requisites  
   
To get started, you'll need the following:  
   
1. **SemanticKernel**    
   Refer to my repository on **Agent Orchestration** for more details:    
   🔗 [Microsoft-Semantic-Kernel-for-Agentic-AI](https://github.com/armeggaddon/Microsoft-Semantic-Kernel-for-Agentic-AI)  
   
2. **Gradio**    
   Gradio helps in building a stunning and interactive chatbot interface. 🤖  
   
3. **Azure OpenAI Compatibility**    
   This project is crafted exclusively for Azure OpenAI subscribers. Features showcased here rely heavily on **Azure OpenAI components**.  
   
---  
   
## 📖 Introduction to AGMO  
   
With the rapid evolution of AI frameworks, we now have **Autogen** from Microsoft, alongside popular tools like LangChain, LLamaIndex, and Semantic Kernel.    
Autogen introduces **Agent Chat**, and one of its advanced concepts is **MagenticOne**, a multiagent system designed for solving open-ended tasks.  
   
---  
   
## 🧩 Components of MagenticOne  
   
**MagenticOne** is orchestrated by the **GroupChat Orchestrator** and comprises the following agents:  
   
### 🔎 MultimodalWebSurfer    
- Functions as a **web surfer** capable of searching the internet and navigating web pages.    
- Uses **Chromium browser** via Playwright for interaction.    
- Requires a multimodal model client (e.g., GPT-4o) for optimal functionality.    
  
⚠️ **Caution**:    
Using MultimodalWebSurfer carries inherent risks, such as:    
- Interacting with prompt injection attacks from webpages.    
- Recruiting humans or accepting cookie agreements without supervision.    
Always monitor and operate in a controlled environment.  
   
---  
   
### 📂 FileSurfer    
- Acts as a **local file navigator**.    
- Can traverse the file system, open, and read common file types and hierarchies.  
   
---  
   
### 🖥️ CoderAgent    
- Provides **coding assistance** using an LLM model client.    
- Generates code based on user instructions provided by the orchestrator.  
   
---  
   
### ⚙️ GroupChat Orchestrator    
- Orchestrates the agents to create **plans** and **action items**.    
- Monitors progress towards goals and dynamically adjusts plans if results deviate or fail.    
- Generates alternative solutions until optimized results are achieved.  
   
---  
   
## 💻 Example Code  

The above agents are available as individual task agents as well in the Autogen Library which can be added as a customized group of agents in the MagenticOneGroupChat orchestrator.

Here’s how to use **MagenticOneGroupChat** with minimal configuration:  
   
```python  
from autogen import OpenAIChatCompletionClient, MultimodalWebSurfer, MagenticOneGroupChat  
   
# Initialize the model client  
model_client = OpenAIChatCompletionClient(model="gpt-4o")  
   
# Create a MultimodalWebSurfer agent  
surfer = MultimodalWebSurfer(  
    "WebSurfer",  
    model_client=model_client,  
)  
   
# GroupChat orchestrator with the surfer agent  
team = MagenticOneGroupChat([surfer], model_client=model_client)  
```  
   
However, the **MagenticOne helper class** bundles all agents together, allowing you to focus on tasks without worrying about individual configurations which is explained below 
   
---  
   
## ⚠️ Important Notes  
   
Using **MagenticOne** involves interacting with a digital world designed for humans, which carries inherent risks. To minimize these risks, follow these precautions:    
  
1. **Containers**: Run all tasks in Docker containers to isolate agents and prevent direct system attacks. 🐳    
2. **Virtual Environment**: Use a virtual environment to prevent agents from accessing sensitive data.    
3. **Monitor Logs**: Closely monitor logs during and after execution to detect risky behavior. 📊    
4. **Human Oversight**: Operate with a human in the loop to supervise agents and prevent unintended consequences. 👀    
5. **Limit Access**: Restrict agents’ access to the internet and sensitive resources.    
6. **Safeguard Data**: Ensure agents do not have access to sensitive information.    
  
⚠️ **Be cautious**:    
Agents may attempt risky actions like recruiting humans for help or accepting cookie agreements without human involvement. Always ensure agents operate in a controlled environment.  
   
---  
   
## 📜 License  
   
This project is licensed under the **MIT License**. 📄    
  
---  
   
## 🙌 Acknowledgments  
   
Special thanks to **Microsoft** for creating the **Autogen framework** and advancing agent-based architectures.    
  
## 📖 Read more
- [Autogen MagenticOne Documentation](https://microsoft.github.io/autogen/stable/user-guide/agentchat-user-guide/magentic-one.html)
- [Research Paper](https://arxiv.org/abs/2411.04468)
- [Source Code](https://github.com/microsoft/autogen/tree/v0.4.4/python/packages/autogen-magentic-one)
