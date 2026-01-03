# 介護A.I. [KaiGō A.I.]

*A voice assistant for neurodivergent individuals, inspired by the caregivers of Japan.*

---

##  Inspiration

> Over the summer of my junior year, I participated in multiple different community service and volunteering activities to gain experience. This led me to interact with numerous different caretakers, mostly of special needs individuals, as well as elders. Talking to them, I identified key issues within their line of work, that I was positive could be solved with a targeted approach to the problem.

It was then that I came up with the idea of KaiGō A.I.. To make sure that it truly answers some of the daily challenges faced, I contacted several caretakers and ran the idea by them. Most were certain that this would be a great idea if implemented properly, while some had doubts regarding feasibility. Nevertheless, I pushed through and came up with an early prototype. I once again asked them to review it, and this time, everyone was convinced.

Incidentally, I chose to name it KaiGō A.I., taken from the Japanese word for caretaker/helper, **介護士 [KaiGōShi]**, as a mark of respect and admiration for these heroes ensuring equality for all.

##  What it does

KaiGō A.I., in its simplest form, provides appropriate answers to a user's query (assumed to be a neurodivergent individual) in the voice of their caretaker, building on previously established emotional connections.

It is engineered to work regardless of internet connection, with a backup **Offline Mode** relying on local computation. It takes two inputs:
1.  A **permanent audio sample** from the caretaker to recreate his/her voice.
2.  A **temporary audio sample** from the user that can be easily recorded through the intuitive U.I.


##  How we built it

I first established a trial version, testing each of the five individual components:
* `Openai-Whisper` for Speech-to-Text.
* `EleutherA.I.'s GPT-neo` for local LLM processing.
* `Groq llama3 78b` (via `groq-api`) for fast, cloud-based LLM processing.
* `CoquiTTS` for Text-to-Speech voice cloning.
* `DistilBERTa` for supplemental NLP tasks.

After validating each part, I integrated them into a `Custom/Tkinter` based GUI, built in Quality-of-Life (QOL) functionalities, and finalized the 1.0 version. The 2.0 version further improved on the GUI, enhancing UI/UX in general

##  Challenges we ran into

* **Dependency Conflicts:** We encountered multiple conflicting dependencies due to deprecated modules used by some components, which had to be manually overridden and patched before operation could be initialized.
* **Component Integration:** Merging five distinct and complex components into a singular, cohesive script was a significant architectural challenge.
* **Performance Bottlenecks:** Initial versions suffered from lengthy processing times, which were drastically cut short by implementing powerful APIs for heavy computation.

##  Accomplishments that we're proud of

We successfully created an end-to-end working application that is task-oriented with a well-defined and clear-cut purpose. We are especially proud of incorporating an intuitive GUI with plenty of information on how to use it, engineered to make sure that absolutely everyone can understand and operate it with ease.

##  What we learned

I personally learned how to implement advanced Text-to-Speech (TTS) with voice cloning into my projects. Furthermore, I gained valuable experience in using multiple different APIs and local modules, making them work together seamlessly within a single application.

## 展望 What's next for 介護A.I. [KaiGō A.I.]

* **Japanese Language Translation:** Full localization and native language support.
* **Mobile Application:** Converting the core logic into an API for mobile device use (iOS/Android).
* **Increased Efficiency:** Further increasing processing speed and efficiency by optimizing the model workflow.
