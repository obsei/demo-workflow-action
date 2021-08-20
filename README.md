# Obsei Workflow Execution via GitHub Action
This repo Showcase Obsei workflow execution via GitHub actions. 
We have created this for [DataTalk.Club's](https://datatalks.club/) demo.

This repo represent following workflow - 
![image](https://user-images.githubusercontent.com/19303690/130244375-693e0ea2-7d71-4a07-87da-e8dc3332885f.png)

 - GoogleNews Observer search and fetch google news article with given query
 - Then TextSplitter split article in small chunks so Classification Analyzer can process it easily
 - Then Classification Analyzer classify chunks in given labels using [HuggingFace zero shot models](https://huggingface.co/models?pipeline_tag=zero-shot-classification)
 - Then Inference Aggregator aggregate classification output for each chunks and compute final inference based on given aggregation function
 - And finally Slack Informer send result to given slack channel using API

Screenshot of final result -
- Full article text
![image](https://user-images.githubusercontent.com/19303690/130246209-91490dfa-3350-4a1e-a502-97e05000d937.png)
- Final article classification result
![image](https://user-images.githubusercontent.com/19303690/130246280-e6941719-abda-42e2-a993-a26e08cc38ef.png)


# How to use it?
- Fork this repo
- Update [workflow.yml](https://github.com/obsei/demo-workflow-action/blob/main/workflow.yml) based on your need (**Note**: Never add you credentials in it, instead use [github secret](https://docs.github.com/en/actions/reference/encrypted-secrets))
- [Optional] Update [workflow.py](https://github.com/obsei/demo-workflow-action/blob/main/workflow.py) if you would like to add some custom code
- Add required credentials in the secret to prevent their exposure to public
- Update github [action.yml](https://github.com/obsei/demo-workflow-action/blob/main/.github/workflows/action.yml) along with required environment variables (For example scheduling at regular time or based on some event refer [link](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions#on) for more detail)
- Spread Obsei love with the world :)


