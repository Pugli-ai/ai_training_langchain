# AI Training - Langchain Basics
In this repo you would find the notebook (`langchain_basics.ipynb`) that contains the basics of Langchain. The notebook is a step-by-step guide to interact with LLMs using langchain.

You would also find a small application implemented with [gradio](https://www.gradio.app/) that uses langchain to generate traveling advice.

## Get Started
Clone the repo:
```bash
git clone https://github.com/Pugli-ai/ai_training_langchain.git
```

And navigate to the directory:
```bash
cd ai_training_langchain
```
The **notebook** is self-contained and you can run it directly.

Instead in order to run the **gradio app** u would need to install some dependencies. You can do that by running the following command:
```bash
pip install -r requirements.txt
```

And then run the app:
```bash
python traveler.py
```
Output:
```
Running on local URL:  http://127.0.0.1:7860
Running on public URL: https://some_url.gradio.live
```

And open the local URL in your browser and you should see the app.

Gradio exposes a public URL that you can share with others to use the app.
