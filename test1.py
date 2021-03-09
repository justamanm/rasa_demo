# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2021/3/1 13:55
# @Author  : Mr.V
# @FileName: test1.py
# @Software: PyCharm
"""
import requests

data = """stories:
- story: My story
  steps:
  - intent: greet
  - action: utter_greet
  - intent: deny
  - action: utter_deny

rules:
- rule: My rule
  steps:
  - intent: bye
  - action: utter_bye
  - intent: bot_challenge
  - action: utter_iamabot
- rule: respond to chitchat
  steps:
  - intent: chitchat
  - action: utter_chitchat

intents:
- greet
- bye
- deny
- bot_challenge
- chitchat

nlu:
- intent: greet
  examples: |
   - hi
   - hello
- intent: bye
  examples: |
   - goodbye
   - bye
- intent: deny
  examples: |
    - no
    - n
    - never
- intent: bot_challenge
  examples: |
    - are you a robot?
    - are you a human?
- intent: chitchat/ask_name
  examples: |
    - What is your name?
    - May I know your name?
    - What do people call you?
    - Do you have a name for yourself?
- intent: chitchat/ask_weather
  examples: |
    - What's the weather like today?
    - Does it look sunny outside today?
    - Oh, do you mind checking the weather for me please?
    - I like sunny days in Berlin.

responses:
  utter_greet:
  - text: Hi
  utter_bye:
  - text: Bye
  utter_deny:
  - text: ok,no
  utter_iamabot:
  - text: "I am a bot, powered by Rasa."
  utter_chitchat/ask_name:
  - image: "https://i.imgur.com/zTvA58i.jpeg"
    text: Hello, my name is Retrieval Bot.
  - text: I am called Retrieval Bot!
  utter_chitchat/ask_weather:
  - text: Oh, it does look sunny right now in Berlin.
    image: "https://i.imgur.com/vwv7aHN.png"
  - text: I am not sure of the whole week but I can see the sun is out today.

language: en

pipeline:
   - name: WhitespaceTokenizer
   - name: CountVectorsFeaturizer
   - name: DucklingHTTPExtractor
   - name: DIETClassifier
     epochs: 1
   - name: ResponseSelector
     epochs: 2

policies:
   - name: MemoizationPolicy
   - name: TEDPolicy
     max_history: 3
     epochs: 2
   - name: RulePolicy"""

url = "http://localhost:8001/model/train"
headers = {
    "Content-Type": "application/x-yaml"
}
resp = requests.post(url, data=data, headers=headers)
print(resp.content.decode())



