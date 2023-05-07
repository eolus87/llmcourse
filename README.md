# ChatGPT Prompt Engineering for Developers (DeepLearning.AI)
## Isa Fulford and Andrew Ng
# Course Notes

The power of Large Language Models (LLM) as a development tool using APIs is still underappreciated. 
This course objective is showing some of the possibilities in order to spark ideas.

There are two types of LLM:
- __Base LLM__: Predict next word, based on text training data.
- __Instruction Tuned LLM__: Tries to follow instructions. Fine-tune on instructions
and good attempts at following those instructions. RLHF: Reinforcement Learning
with Human Feedback. Helpful, Honest, Harmless is the goal of these models.

This course focuses on __"Best practices for Instruction Tuned LLM"__.

When using instruction tuned LLM, think of it as telling some instructions to 
a colleague. When they don't work, normally it is because the prompt is not clear
enough. You can specify the tone as well, indicating it will help with the prompt.

## Guidelines
__Principle 1: Write clear and specific instructions__. Clear is not short!

    Tactic 1: Use delimiters -> Triple quotes, triple backsticks, triple
        dashes, angle brackets.
    Tactic 2: Ask for structured output
    Tactic 3: Check whether conditions are satisfied. Check assumptions required 
        to do the task.
    Tactic 4: Few-shot prompting. Give succesful examples of completing
        tasks. Then ask model to perform the task.

__Principle 2: Give the model time to think__

    Tactic 1: Specify the steps to copmlete a task.
    Tactic 2: Instruct the model to work out its own solution before
        rushing to a conclusion.
    
__Model Limitations: Hallucinations__, things that the model has not been
trained on, but it can make them up and sound plausible. Be aware that
it can be pretty realistic.
    
Recipe for reducing hallucinations:
1) First find relevant information
2) Then answer the question based on the relevant information


## Iterative Prompt Development
The process of getting into a successful prompt can be complex. The 
cycle is similar to Machine Learning, where we start with an idea,
we implement it, experiment with the results, check the errors and
come back again to the Idea.

Prompt guidelines:
- Be clear and specific
- Analyze why result does not give desired output
- Refine the idea and the prompt (Clarify instructions, give more time to think)
- Refine prompts with a batch of examples
- Repeat

__There is not "golden prompt", it is likely you will need to refine it.__

## Summarizing
There are too many sources of data and not enough time to read them all.
One of the main advantages of LLM models is summarizing!

Main things are:
1. Description of the text that is coming. 
2. Instructions and details that you want the model to do.
3. Clearly stated where the input data is with a header and the delimiters.

## Inferring
The model takes the data and does some kind of analysis. Sentiment extraction,

Instead of training a model for every task, in this case it is just
changing the prompt or the interaction, so that can hugely improve the 
speed of development. Some interesting examples are presented:
1) Sentiment detection/analysis
2) Data extraction (product name and company)
3) Extract data from text formatting the answer
4) Infer the topic of the data

## Transforming
Transformation inputs into another format (language, grammar, format...).
Some interesting usages are:
1) Language translation (it might be wrong!)
2) Language detection
3) Universal translator
4) Tone transformation
5) Format conversion
6) Spellcheck/Grammar check

## Expanding
Taking a small piece of text and get an LLM create a bigger piece of text (like an e-mail).
It is very interesting as a brainstorming partner.

Careful with the usage here, it needs to be reminded that the content has been
created by a LLM Chat bot.

Explanation of the parameter __temperature__:
- The lower, the more reliable and predictable and static.
- The higher, the more random, creative, different the response will be.

## Chat Bot
LLM are stateless, so if you want the model to "remember" any previous answer, they need to 
be provided as context. 

The main idea is that a function is required to gather all messages coming from user, 
system and chatbot so the history is maintained. There is an issue here not tackled by the course
regarding the size of the queries that are ever-growing.

It is recommended using low temperature for ChatBots, so they are not "too creative".

## Conclusions
It goes through the contents of the course as a summary.

