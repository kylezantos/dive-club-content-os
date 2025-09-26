Vitaly Friedman (00:00.27)
That's okay, that's okay, I think one interesting point that I wanted to bring up here as well is that it's not just that people are somehow frustrated by AI. I think this is maybe not quite the context of framing around it. I think that in some way they just want to be able to rely on it at least to some degree. And the problem is that...

Dive (00:00.518)
But who knows? just want to be 100 % sure.

Vitaly Friedman (00:28.63)
A lot of the times when people are using, and this is something that we kind of learned, which was very, very surprising, people don't like to admit that they're using AI. So when you're actually looking at people and how they behave at work, if you're working in finance, if you're working in insurance companies and stuff like that, you will never hear anybody saying, well, I used AI for this or I used AI for that. Because to many people, it doesn't feel like this magic anymore. It feels more like, this is inaccurate potentially. This is...

hallucinating or this is maybe not good enough. And of course people are not perfect. I mean, we always have this comparison between people are not accurate either. They also make mistakes, right? Yes, but AI is a part of software and people are used to the fact that software is predictable and reliable and AI isn't, right? And so when you own all of a sudden get to the point where you have an AI feature and you want to use it, right? And you use it maybe for your work.

then it's on you to verify if it's reliable and if it's correct and accurate and all of that. And that's a lot of work again. So we have this different cost that people are carrying on the one hand interaction costs where they need to be interacting with it to check sources and stuff like that. And the other hand, articulation costs where you have to explain to AI what you actually want, right? And then even when you're iterating or interacting with AI in this space, then find that

There is a lot of time that people spend cleaning up after AI, really literally mopping up the errors and mistakes and hallucinations and all of that that come up. And that is tremendously expensive in terms of time. It's probably still faster than if you type it from scratch, but it takes a remarkable amount of time. And so in my book, a chat bot or text box experience alone would probably be...

definitely not very high on the list of what to do with AI. There are many other things we could do as well.

Dive (02:23.344)
I want to get into all of those. And even before, like I want to go back to something that you talked about, which was how all of the burden for having a good interaction with AI is basically on us right now, where, man, just the value that can be created when you flip roles and AI asks you questions is amazing. almost everybody I talk to, especially people outside of tech have no idea that that's even possible. Like that's not in their frame of reference for

how this interaction can look like. I'm like, man, that's probably over half of what I do with AI is just give it a prompt and I say, ask me a bunch of questions and then we'll make a thing together. And so how can we design affordances to help people even understand that that's possible?

Vitaly Friedman (02:57.154)
Yeah.

Yeah, yeah, exactly that.

Vitaly Friedman (03:04.941)
I mean, it's, so this is like an interesting story because if I can actually share the screen, I can share and show that. think there are a few, I mean, what's really important for me, because we went to start, is that many of those things are remarkably simple. There is no big magic. It's like, it seems like we are so obsessed with being AI first that we're forgetting about the good old things that people are used to and people know and understand because it already lives in the mental model. And so when I look, let's say, at...

Now let's take a look at the shared GPT for starters. So I'm going to go in here and share the screen. And you see the screen now, I think. And so if we go and let's say and explore something like, I don't know, like if I can go into deep research mode, I cannot. Excellent. But if I say something like, useful design patterns for AI interfaces.

And so off it goes and it gives me that list. Typically when it comes to deep research, right, and if it thinks longer, maybe switch over. Okay, that's not probably going to ask me anything. Let me just change it to reason, although it's not necessarily the something I would like to do here. It's going to start thinking and eventually, no, it's not. But if you go into deep research mode, typically it will ask you kind of a bunch of, there are a couple of sentences, right, asking you.

Do you want this? Do you want that? And so on and so forth. And usually what you get there is basically a list of questions that would appear very much like this. And then what you need to do with that is you copy paste all of that back into the text box. And then to each of them, most people would say, yes, I want that. And no, I don't want that. This kind of story. Why? I mean, why on earth would we do that? If you go to the safe of complexity,

Dive (04:51.696)
Yeah.

Vitaly Friedman (04:56.059)
And I do the same thing. I'm to ask the same thing over here. Find useful design patterns on the interfaces.

Dive (05:01.978)
I make it list bullet lists. I make use, use numbers. I specifically say use numbers because then I can refer back to the numbers and I don't have to write the whole thing. Cause if you don't have numbers, then it's like, what are we even doing here? Yeah.

Vitaly Friedman (05:03.861)
sure. yeah, yeah, yeah.

Yeah. Yes, References, this is what we usually call references. So if I go in and say research, now it tells me, hey, do you want to add some details or clarifications while it's actually working on it? Because very often people forget some critical details. And so then they have to wait until AI is done to then provide extra details. And here I can say for accessibility, right?

And so it actually does the work and then it adds that layer, that extra information to it. So that's already solved this problem of actually being able to add something while AI is thinking, although it doesn't really, really think. So there is that. But there are, of course, other things that we could do at this point. Because I think in many ways, this articulation that we have to do here, it's just totally unnecessary. Because again, this is a wonderful example that comes from Nikroblevsky in which he wrote about this pattern here.

Dive (05:38.3)
That's great.

Vitaly Friedman (06:05.198)
And basically the idea is very simple. We kind of have a task builder. So what do you want to do here? I want to ask or search or explain or something else. And maybe I want to integrate it into Slack or Gmail, Salesforce, and something like that. And maybe I want to make something out of that. So if you think about this, you can actually frame it into some of the frequent tasks that people are doing. You can say, you know what, summarize a Slack channel and turn it into a Word file. Right?

or maybe analyze some data from Salesforce and turn it into a PowerPoint. Right? So click, click, click. And what happens in between though, is that while you have selected that, say, you what was that one? Search Notion PowerPoint. So I want to search in Notion and make a PowerPoint. So you can say, well, let me create a template for you. So this is a prompt and of course it could be extended and augmented.

Search my notion for a particular topic that's something that you have to provide and create a PowerPoint presentation summarizing the findings. Click, click, click, you write your topic, done. And then you basically get the results, right? So it's kind of like task planner, if you like. I think that's incredible, right? In other ways, I would also say that we can do much more than that. One really nice example of that is consensus. I love, I mean, I love consensus in so many ways.

Dive (07:10.299)
Nice.

Vitaly Friedman (07:27.274)
If somebody is not aware of consensus yet, this is really, really great example of really good AI experience. So let me guide you. I mean, this is like going all, I'm getting too excited about this, I guess, right? But let's say we are looking for something. I don't know, like let's go for some sort of drive research. I'm not obviously expert in any of that, but let's just go for that. And so just pick one. And so it goes in and it actually going to try to find out to those things. That's not very surprising.

Dive (07:38.074)
Great.

Vitaly Friedman (07:56.414)
And that's all that thing for me. Beautiful. What I absolutely love while I actually working on that, let me come back and show it over here. What I love is it actually takes the good old fashioned stuff that we love and care about, like filters, and it offers them for you right here. Isn't that amazing? I mean, for me, it's like, why don't we have it everywhere?

Dive (08:14.288)
Mm-hmm.

Dive (08:18.372)
It's so funny because the pattern is so familiar and yet I don't think I've actually seen it in relation to an AI chat before. Yeah.

Vitaly Friedman (08:21.068)
Yes, I have never seen it in any kind of AI experiences before. So sure, you can ask anything. You can ask any kind of question. But what if I want to just specify it? I want to say last five years, and maybe I'm looking for at least five citations, and maybe a particular journal rank, and maybe a particular methodology. I want to see only, I don't know, observational studies, and maybe case reports, and whatever, things like that. And you apply it. And then you execute a query with that.

That's infinitely more useful than just saying, ask me anything. It's a simple thing, but it actually makes quite a difference. And once you get the result here, obviously you get these citations and all that, and so on and so forth. That's not very surprising here. But one thing that they do have, which I find quite impressive, is consensus meter. Because the problem with AI is that usually it gives you just an answer. So you ask it a question, it gives you a statement, or it gives you an overview.

But why doesn't it give me distribution of overviews, so distribution of statements? So the idea behind it is, okay, does urban heat island effect reduce accuracy in electricity peak forecasting? You know what, I'm going to look at all the papers. Damn it, I cannot do that because there are not enough.

Let's see, maybe this is going to help.

No? Damn it, I need to pick something that's a little bit more... Well, no, let me just take maybe this one here. I'm running out of credits. no, already? That's disappointing. Hold on just a second. Let's see, consensus meter. Let me take this one. Here we go. Maybe that would be better. Okay, so that's better.

Dive (09:43.676)
Yeah, you're good.

Vitaly Friedman (10:07.978)
Not my day today, maybe. Hold on for a moment. Let me just take something else. But let me just pick something that's out there. Like this is probably quite hella quick. Yeah, I guess so. So, and maybe yes, I will even get something, right? So you kind of get the distribution of what papers tell you, right? 95 % of papers indicate yes. And if you are, one of them is indicates possibly, right? And there is I guess none that indicates no, right?

Dive (10:09.565)
You're good.

Yeah, yeah, you gotta go real generic here.

Vitaly Friedman (10:37.57)
So those things are helpful. And then I kind of like this layering. So on the one hand, typically in AI experiences, we have the sources and references and stuff like that. But here, they're also color coded. So green meaning this is OK, confirmed. And yellow, if it comes up somewhere, means that it's not confirmed or there are mixed opinions on that. So those things are little things that are really, really impressive. And then.

Dive (10:59.654)
Hmm. Mm-hmm.

Vitaly Friedman (11:06.434)
You can also filter that part. You can filter that output by a particular sentiment as well. We should not forget that filtering, sorting, searching, and all of that stuff is great. We shouldn't be just dismissing it for the sake of AI first. If anything, we should probably be leaning more towards maybe AI second. Just bring the good old-fashioned filters. Filters are great. I would love to see more filters in the AI experiences. And it's not hard to do. It's just...

Dive (11:35.067)
Yeah.

Vitaly Friedman (11:35.434)
Under the hood, basically augment the prompt with some specific details that you want to be respected or so. But it cannot be just generating text. It must be actually really doing some sort of, but must be some sort of a combination, I guess, between just an AI that just generates text and something that actually tries to understand and categorize and classify. So that's a little bit more complicated, of course, than just regular systems. But I think it's

It's incredible. This is what I want.

Dive (12:06.556)
That was the thing that stood out to me is even just differentiating from this isn't a bullet list. We're not operating within this mental model of a back and forth or a dock. It's there are controls and UI and it's all very familiar. And yet again, I haven't seen it very often in these new AI products. I love illicit.

Vitaly Friedman (12:14.904)
Yep.

Vitaly Friedman (12:28.086)
Yeah, I think it's, yeah, this is great. There is also one more thing that is often missing because remember, one of the main challenges that we have is that we have pretty poor accuracy, right? Not even accuracy, I would say, that a lot of people are assuming that there will be some hallucinations and it's not very clear if you can trust something or not. And so a lot of time, this sort of fixing errors or refinement journey or verification journey, whatever we want to call it, takes time. But then what I absolutely love about Elicit,

And it's fantastic, the way, you never, dear friends who is going to watch this later, if you never heard of it, it's a really, really fantastic, also well-designed AI tool. It does a couple of things really well. And first of all, it really tries to be accurate. So it gets the sources, and then it screens those sources for specific criteria that you might can select, and then extracts data from that. But what I love most is these asterisks. Mike, what are these asterisks?

Dive (13:23.784)
Yeah.

Vitaly Friedman (13:25.524)
They are magical and that to me that's truly magical because typically this would be just references to some papers. But that creates a burden again that leaves on the user's shoulder because they now have to go to the paper and find a place where this is mentioned. Instead they're linking directly to a particular segment of that paper that indicates where this comes from. So this is direct, like literally direct linking to the segment, not even to the paper.

Dive (13:53.926)
So good.

Vitaly Friedman (13:55.444)
And then you can also go through a couple of mentions there to see where it's actually coming from and why it's coming here. So, and this to me is... I this is how it should be. Right?

Dive (14:09.36)
Yeah, because I'm just looking at the references and I'm like, well, do I recognize the URLs? I'm like, okay, it's probably good enough. Like I trust it. I'm not going to put in the effort of actually clicking on them.

Vitaly Friedman (14:13.622)
Yeah, yeah, yeah. Yeah. And I think that's also like one thing that's really important here is that there is no emphasis on chatbot and so on. Yes, this is a center stage experience where you have to type, right? Or have to choose a topic that you're interested in. But there is no chatbot here because at this point you are exploring the data that is in front of you, right? And sure, you can bring back that text box in some way, somewhere. I'm pretty sure about that.

you're kind of more in the proper exploration research mode at this point, right? And I like that as well. And it goes also, of course, for all the other things. And I think this is incredible. This is why I think those kind of experiences, they're totally different. They are unlike the traditional chatbots at all, because they really provide an enormous speed up for people who just need to understand something and don't have the time to go through papers on their own. But then...

Dive (14:49.296)
Mm-hmm.

Vitaly Friedman (15:11.98)
This really backs up certain ideas and concepts and statements that are being then explained here in Elicit. So that's great.

Dive (15:24.188)
remember going through Elicit, I mean, it was probably close to a year and a half ago. And it was really, really impressive because it did feel like, wow, they did not just slap a chat on. Like AI is in the very fabric of what this product is. And the moment that I really felt that was, I think they had something, it might've changed, but when you were even setting up a research study, you could use AI to customize the columns. So you're getting structured data, but you're using AI to...

Vitaly Friedman (15:49.646)
Yeah, yeah, yeah,

Dive (15:52.316)
to structure your report and you're not having to think about it in terms of this perfect prompt inside of an input. It's like, no, no, no, there's this familiarity of a spreadsheet, but now I'm just answering isolated questions of what data do I want at the column level. And I saw that and I was like, oh man, that makes so much sense.

Vitaly Friedman (16:05.614)
Yeah, yes. Yeah, we don't have that either. think that what I started doing, and I think if I look at my perplexity, because I started setting up these sort of preferences and customization settings, so personalization, I think it's here, when I basically ask it to show results on a data table whenever it can.

Dive (16:28.523)
cool.

Vitaly Friedman (16:29.292)
I just find it very useful. And so this is just sort of like a prompt that is being then submitted with every query that you send. So you can find it in ChatGPT, can find it in Proplex, you can find it everywhere. Kind of just a way to tell AI what it needs to know about you to respond to queries better, I guess, right? And I take it very seriously. So this is something that I try to review as much as I can, but it's limited in space, so we can't do much there. But...

I take it very seriously. It's like every word here is, I am trying to be quite careful with that.

Dive (17:05.582)
Even this text box is an interesting example because I'm looking at this and like, yeah, that all makes a lot of sense. I want most of that. yet so often my preferences boxes are empty because I genuinely like, I don't know what goes in there. I'm sure I could figure it out, but I would have to probably interact with a different AI to even figure out what should go into this chat box. And it's like, like Dia, for instance, my preferences are basically empty right now. And I wonder

Vitaly Friedman (17:17.23)
Mm.

Vitaly Friedman (17:27.318)
Yeah, yeah.

Vitaly Friedman (17:31.35)
Mike, we know exactly what you're doing after this.

Dive (17:34.426)
I know, right? But like, if there was a heaven forbid, a wizard, you know, with some old school affordances that asked me some questions, I would take the time to fill it out. I think I would just, I just need a little bit more hand holding because then it feels intimidating otherwise.

Vitaly Friedman (17:49.334)
Yeah, I mean, it's kind of really brings me back to also this here. This is a wonderful resource. I don't know why so many people are not aware of it. This is fantastic. This is coming from Luke Bennis. Luke Bennis has been coming up with a couple of ideas about what could be a really nice AI experience. He has some really nice ideas in there, like, for example, something like this is probably something that you would appreciate, So the idea is a bit of hand holding, indeed. So when you're writing a prompt, right?

Before you even start writing here, you can be asked something like, OK, so what do you want? Maybe there is a reference, maybe there is a particular level of expertise that you're expecting or anything like that. And again, these are just old-fashioned UI controls. But why do we feel like they not needed anymore in the age of AI? I think that something like that would be incredible. On the other hand, he is even suggesting something like this, which I think is really, cool, too.

Dive (18:20.443)
Brilliant.

Vitaly Friedman (18:46.798)
which is sort of assisted authoring for prompts. So you maybe start prompting here, and then you have an AI assistant that operates on that level of the text that you have provided and say, hey, let me make it a bit more succinct. Let me maybe add more specific context. And maybe I can ask what kind of context it needs. Like, for example, write and present for whom. Are you looking for a presentation to executives, for designers, for, you know, maybe you want to just specify that. Just ask a few questions. I think that...

Dive (19:15.718)
Mm-hmm.

Vitaly Friedman (19:16.438)
My ultimate goal is, and this is what I'm trying to kind of get to, is before anybody sends a prompt, the purpose should be to make it so succinct, so accurate, so useful, so detailed, so contextual that the chance of getting a very generic and not very helpful response is minimized. So I want to maybe slow down people in prompting.

Right? Slow down people and actually sending something to AI system because obviously it's like, it doesn't come for free first of all, because of sustainability. But then on the other hand, it also takes time, like 20 seconds, maybe 30 seconds, depends. And then you have to look through this wall of text and then you realize that something is missing because the answer is not at all what you wanted and you're missing like one important keyword in there or something like that. Then you start all over again. People are wasting an enormous amount of time going back and forth with this AI output just because they miss something.

So maybe we could do a bit of hand holding indeed, or just say, hey, hold on for a moment. Do you mean this or that here? On the level of the prompt rather than the level of the output. I'd love that.

Dive (20:22.886)
Yeah.

Dive (20:28.092)
I totally, because this is the perfect example of, I don't know, that prompt to me is it's a very novice prompt, you know, but it's still the majority use case. People go into AI and they say, make me a thing. And if you lead with a verb, the AI is gonna make something, you know, it's always gonna make something. And this would be the perfect example where with a little bit of understanding of how prompt engineering works, you probably would say something like, my goal is to create an annual...

Vitaly Friedman (20:36.161)
Mm.

Vitaly Friedman (20:44.608)
Yeah.

Dive (20:58.032)
Don't build anything yet. Line break. Let's have a back and forth. Ask me questions and get all of the context you need. And at the end of it, you understand how to be a prompt engineer. So be the prompt engineer and write the thing that's perfect for you. That gives you all the context you need to make something that is good, but like maybe 0.1 % of the worldwide population understands that that's the interaction that you have to have. So how do we productize that?

Vitaly Friedman (21:00.813)
Yeah.

Vitaly Friedman (21:11.904)
Exactly. Exactly.

Vitaly Friedman (21:21.31)
Yeah, absolutely. think that it's like the story there is like when we are looking at all the frameworks for prompting, in many ways they have a particular structure, right? So why don't we just replicate the structure in a way that people don't have to remember it? Like, for example, this is another pattern from here as well, which I think is great. Maybe we should do just that. Maybe this should be the start of the AI experience rather than a chatbot with open the Xbox, right? Hey, main prompt, context, background, output details. And you know, sometimes you say,

act as a UX designer, or act as a financial advisor, anything like that. So maybe we should have that structure somehow reflected right here, so as you write it, you know what to write. Because if it asks you, ask me anything, so what are you supposed to do exactly, and how would you structure that? So this, think, is really, powerful. I those little things are not difficult. It's just UI stuff. It's really not hard at all.

But then you're augmenting whatever people are looking for with this stuff in the most structured way and give them sort of a structure to operate within. And then you end up with a better experience as well because the input is better and so the output will be better as well.

Dive (22:34.554)
Anything else on chat bot land before we, it's kind of like a broader spectrum of AI things that I want to get your take on. But this is like one of the main things that I'd love to hear you talk about. So I'm curious if there's anything we haven't mentioned.

Vitaly Friedman (22:42.573)
Yeah.

Yeah, I think to me it's really slowing down the people when they are trying to articulate their intent is really, I think, important. We tend to... Because the thing is, if they are fast in the beginning, then the slowness of AI really breaks this experience for them. But if we kind of keep them for a moment and ask them something that we need to know in order to give them a better response, then it's actually a better place. The only thing I would say...

Dive (22:57.553)
Yeah.

Vitaly Friedman (23:15.562)
is that maybe I have an example of that as well somewhere. I think that this is really something that I wish more websites were doing as well. I just need to find it briefly. here we go. So this is also something that Perplexity is doing right here. Can you see the screen? Yeah. So when you're asking something like what are common patterns and heuristics designers should be thinking about when working with the AI products, instead of asking you to type, it gives you radio buttons.

or checkboxes, whatever. I mean, this should be it. Instead of saying, answer that question, then answer that question, then answer that question, you can just go and say, boom, boom, boom, boom, boom, go. And if you want to skip, you should be able to skip then as well. So if it kind of really slows you down in that way, it's not like you have to type all the time, but you just go. Because very often what we see is the opposite. We see that when you start deep research, JGPT, for example, before it even goes into deep research mode,

Dive (23:48.922)
Yeah.

Vitaly Friedman (24:14.156)
It will tell you, well, before I even start doing the deep research, here are a few questions that I would like you to answer. And then there may be six or seven or eight questions. And then you have to copy paste them all into the text box and then answer each of them. But why don't you just give me, I don't know, radio buttons, text boxes, sliders instead for each of those. I can answer directly without copy pasting anything. I can basically select and choose my journey and then off you go and you can do your thing. Right. I think in many ways this would be remarkable.

I mean, I just would love to see more of that. Another example that I maybe just want to show is we're kind of moving away from chatbot towards something that's maybe a bit more like a long spreadsheet. Or you want to add something? Yeah, sure.

Dive (24:47.526)
Yeah.

Dive (24:55.93)
Well, I want to add something because it's like.

something that comes up a lot is this idea of a dynamic interface, something that AI is generating on the fly. And it was like all the rage and then it's kind of tried it down a little bit and people are like, you know what, actually predictability is nice. And yet for that type of interface that you were showing with perplexity, this is where it's like kind of the sweet spot where dynamically generated interfaces that have the sole goal of context extraction, that is like killer because

Vitaly Friedman (25:19.702)
I think so, yeah.

Dive (25:28.216)
you're always going to only need the most basic, like atomic components that users are already familiar with. And you're just tailoring some kind of a set of controls to get people to be a little bit more specific about what they want. That feels like, yeah, you might see that in almost all of these tools here soon.

Vitaly Friedman (25:46.382)
Yeah, I hope so. mean, it's also kind of the story about how exactly we capture users context, right? Because in the end, it's all about that, right? It's just all about that. I mean, there are different parts of the journey, right? Where obviously people need to articulate, then they need to be going through this wall of text, right? And then they need to do something with it. Very often they want to extract or they want to compress or they want to expand. Like there are many, there's a lot of tweaking here and there that is happening too, right?

because they just want to get to the right thing, whatever that is, and maybe send it to a manager or create a presentation or something, but they want something valuable. And I see in testing, it's so funny because people take the output from AI and then they look at it and read it and check it and verify if it's all right, more or less or not. And then they cherry pick. They take maybe the first paragraph and then the second and maybe the seventh and maybe the 12th and they pull it all in a separate place.

like maybe in a text editor or something like that. And then they do the editing there. And then they bring it back to Chatter, Chatter GPT or so to summarize it for them and restructure it in a meaningful way. This is weird. Whenever you have a dedicated space for what they're doing here, that's not great. We need to reduce the distance between where people want to do something and when they do that. This is like the most obvious thing ever. Probably the most obvious thing I've ever said.

But this is really important because ideally I would love to be able to have an option to just if I go back to ggbt here to say hold on for a moment. I don't need this. Can I just remove this part? Well, I cannot because I can just have a conversation about that. So I need to bring it copy it somewhere and then move from there. But again, coming back to perplexity and I kind of like perplexity for a lot of things can say hold on for a moment. Let me kind of go into editing mode. It might be just not as visible or not as clear. You can say converted to a page.

Dive (27:26.704)
Mm-hmm.

Vitaly Friedman (27:40.654)
So once you do that, it kind of goes through it and it kind of creates an article or a page on that topic, right? But what's important for me is that it has a table of content that you can navigate within. So we'll see in a moment here. So you can jump to a specific area. While it's working, maybe, this is kind of something that you also see here on consensus, by the way. You have this way to navigate. So if I ask a separate question, right?

I can go and jump to that question or to the previous question. I can really kind of navigate between that response, right, within that response, right? And then in here, back then, back to complexity here. So I get this text being generated. So it takes a while to write, I guess. Eventually it will be done.

Dive (28:24.38)
The biggest change with AI is the importance of loading states.

Vitaly Friedman (28:28.736)
Yes, loading states are very important, that's for sure. So it's probably going to take a minute or so. But the point here is, and I find this actually quite impactful, that you will be, in a moment, able to do something that you, I don't think you can do anywhere else because of the way of how it's actually designed. Because it kind of, I think it really maps well into how people use AI as well. But for that, we just need it to be done. Maybe I can just stop it. Here we go.

Maybe I can do that here. Can I have a conversation? No, it's just stopped altogether. That's disappointing. Okay, I'll have to restart it. Can I? here we go. we go. Yes, it's broken somehow. This is not what was supposed to happen. Let's see. So basically it kind of gets into, I don't know why this happened. This is supposed to be context menu where you can actually add list.

Dive (29:07.676)
Yeah, you're fine, We're not in a rush.

Dive (29:26.382)
Yeah, you can see it. It's just missing the background.

Vitaly Friedman (29:28.81)
Yeah, I'm not quite sure why I guess, maybe because I broke it. But the point is of this, right, and can say now, go and say, let me just change that, maybe remove this part or extend this part or do something with it, right? Can I extend more? Okay, so it probably will be extending. Maybe, I don't know, I probably broke it at this point. Yeah, so it will, right? So kind of really operate on the level of that output, right?

Dive (29:53.073)
Nice.

Vitaly Friedman (29:57.398)
which is something that you cannot do much in other places. So this is nice. And then you can, of course, also say, I want to move columns around and add some sections and also have this little different use. I want to have a table on something. Why isn't this everywhere? Like this. It's simple. want, instead of saying, please write down in a list format or in a table format or anything like that and make it compact or something,

Dive (30:13.006)
Yeah, I have not seen that.

Vitaly Friedman (30:26.508)
I think that this should be everywhere. I mean, just everywhere by default, like in every single AI experience because it depends of course on where it's used, but I think it has incredible value. I mean, maybe not this because you're kind of adding images or so, but this and maybe this is great. So I'm a little bit obsessed with this because I think in some way I feel like we can do so much better.

Dive (30:29.594)
Yeah.

Vitaly Friedman (30:55.234)
I mean, this is not difficult stuff. I mean, by no means. This is something that we just forgotten to use because we're getting a little bit too excited about AI.

Dive (31:03.964)
Hmm. I could see maybe like an auto at the beginning where it's like, okay, if you don't want to make the choice, fine. We'll, we'll do the best that we can, but this is such an intuitive little control that I would use it every single day.

Vitaly Friedman (31:08.264)
Maybe, Yeah, yeah, sure, sure. Of course.

Vitaly Friedman (31:17.28)
Me too. Yeah, so that's kind of the part of the story. think there is a lot of innovation, I have to say. So it's like really moving very, very quickly. I like, for example, in Gemini, when it's searching for, I don't know, how do windmills work, for example. Right. And I go in here.

It also takes a bit of time. You see, they're like always waiting and we're kind of taking this for granted. People are very impatient. If anything, they become way more impatient over the last couple of years. And so what, yeah.

Dive (31:43.386)
Yeah. It what's interesting. Sorry. I like, I'm almost now wondering if this is the right place for some of that context extraction too. You know, like you almost assume that you have this first lightweight prompt and it's like, can you already get information that you would feed into the next prompt while you're processing the first one? And I bet people would be totally fine actually waiting much longer. It reminds me of something that the gamma head of design said.

Vitaly Friedman (32:03.766)
Yeah, sure.

Vitaly Friedman (32:12.684)
Mm-hmm. Mm-hmm.

Dive (32:13.018)
And he talked about how when presentations were being generated, they then prompted people to work on the theming and you can like change some of the theming controls. And then people, all of a sudden they didn't care about how long it was loading because it took, gave them something to do. Maybe that's the place to get some of that extra context.

Vitaly Friedman (32:20.371)
makes sense. Yeah, absolutely.

Vitaly Friedman (32:25.884)
Yeah.

I mean, in the case of Perplexity, they're just asking for more context as well. So this is like, we can keep people waiting, or we could give them something to do to create a more meaningful output. So that makes perfect sense to me. I mean, one thing that I really liked about Gemini is that they have this one thing. Where is it? I think it was maybe not in every model. Oh, no, they do. They have double check response button.

And I was like, for a moment, I was thinking, what does it mean? So we should click on it. So it basically tries to go through its output, right? And try to find any sources that actually back up whatever the check is doing. So if there is anything, no, I don't see any highlights here. Typically, right, it becomes green if Google found content that's slightly similar to the statement and something that's slightly different from the statement is highlighted this way.

You just usually it's highlighted, but here it doesn't highlight anything at some point, I guess. So that's a little bit disappointing. But you're gonna get the idea. I can try to verify sources to make sure that it's actually right. So for example, sure, hallucinations is something we cannot fix yet. But if you could say to JGPT and Perplexity, you know what, go for all these links and just make sure that they exist. Or maybe it should actually be a default mode anyway. Although it probably would take a bit more time there too.

Right, those things are very, very simple adjustments and refinements, but I think that they all compound over time. So once you bring the selection of a format, once you bring more content, more structured prompting, once you bring a better way to navigate the output, once you bring in the distribution of results rather than just a summary, those things really compound. I mean, ultimately, Mike, if I'm being honest, I just want to see AI products.

Dive (33:59.494)
Mm-hmm.

Vitaly Friedman (34:21.868)
that people fall in love with. And I don't see people falling in love with, I mean, I know that Perplexity, people working on Perplexity and Claude and many others, they absolutely love the tools. But I want people to feel, wow, that's absolutely amazing AI experience, or just experience, because people don't think about it this way. I want them to really be helped, right, to find a lot of value so they don't waste time in front of the screen. Navigating through the output,

finding the ways to copy the text, to edit the text, to tweak the text, to bend the text, to ask something else, to add more context. It's a story. like, it's usually takes quite an enormous amount of time, which is very often just maybe not necessary to do.

Dive (35:06.758)
Yeah.

Vitaly Friedman (35:10.146)
I'm getting too excited on that.

Dive (35:10.31)
Something that I've been doing. Yeah.

something I've been doing a lot when working through these different system prompts and the only product that I'm working on is having the AI assign confidence scores to basically everything that it does, because then you can do all kinds of different rules where maybe it's like, automatically pull out things below a certain confidence score and maybe we can perform some action on them. And it like is effective, but it's again, you have to think of that, you know, you're figuring it out like on your own.

Vitaly Friedman (35:24.622)
Mm-hmm.

Dive (35:44.806)
how to use AI, how to get the most out of AI. And this simple thing like the double check results is one of the main things that I then do when I have those confidence scores. But you almost have to build an entire system to handle the raw output in order to achieve some of these results that could very easily exist in the core UI. And then you can attach affordances that go beyond the simple bullet points with like, you if I was doing this in Chatchapotee, it would probably give me a little check emoji and an X.

emoji or something in between, you know, but that simple highlight, well, that doesn't exist out of the box.

Vitaly Friedman (36:18.552)
Yeah, but I think it's from what I've been looking at when I was kind of preparing for the course. I was looking for ways to do that and it seems like it's actually quite difficult to do because it actually has a lot to do with the way of how prompt is written. So if you're missing a specific detail, then something that's actually accurate will or might be perceived as inaccurate.

because AI doesn't really understand, doesn't have a notion of truth. So it's like, it's looking at what you are asking and because very often the prompts are not detailed enough or not precise enough or don't provide enough context that might be relevant to you, then it's actually very difficult to even be in a position where you can say it's accurate or it's not. But I I just haven't seen.

a lot of tools that are giving you this sort of precision and accuracy are trying to do it well or kind of do that well. I think that's maybe just a very hard problem to do. Like the same thing with forgetfulness, right? As you have longer conversations, eventually AI just starts forgetting things. I think many of us have experienced this before. It has to do with the context that an AI model can typically remember, the context window.

Dive (37:14.747)
Yeah.

Vitaly Friedman (37:34.606)
That's not something you can solve really easily. mean, it just eventually if you let's say throw in a bunch of stuff at the AI and like really long text, then if you keep going with the conversation eventually it just starts forgetting things. Although some tools I think try to do this thing where they kind of try to summarize whatever has been said before and feed it into themselves, but then they still miss the context. And the problematic part is that very often or very often usually AI doesn't tell us that it's out of context, it's out of.

Dive (37:37.787)
Mm-hmm.

Vitaly Friedman (38:04.032)
memory. It just keeps going and it goes wild suggesting things and assuming things and filling in the gaps, filling in the blanks I would say with just whatever it feels is plausible. And then off you go, the conversation goes off track and then you get very little value from that.

Dive (38:04.42)
Yeah.

Dive (38:22.556)
it's a low hanging fruit pro tip is always ask where we're at on this context window. Like, are we buttoned up against it?

Vitaly Friedman (38:27.308)
Yeah, but then I mean, I mean, the point that I'm bringing this up here is it might be actually not a bad idea to have something like an indicator somewhere in right up a corner, something like, you are over limit or just give people some limits to operate within, right? Because again, the context windows are not very small at this point, but of course, if you keep a very long conversation, then you drop in a bunch of, I don't know, text files and Excel files and whatever.

Dive (38:35.676)
I

Vitaly Friedman (38:54.87)
eventually you will hit the limit and then off you go. So, I mean, we need to just maybe explain to people a little bit about and be honest about that, about what's happening. The same story for me is when I see a lot of chat bots that pretend to be humans, but are in reality just AIs under the hood. It's just, it really breaks everything. I mean,

Just tell people that's AI, because typically people speak to humans differently than speak to AI. They can tell right away. We cannot tell in text necessarily or in images or in videos if it's AI generated or not, although some people have a smell for it somehow, right? But when it comes to interaction, like a chat interaction, people can see through like right away, because if, like, for example, if you think about this, people usually write in chunks. They can also write something like, or no.

Dive (39:33.531)
Mm-hmm.

Vitaly Friedman (39:49.912)
for sure, never gives me that. AI is always, well, in the light of the recent developments and whatever and so on and so forth, and it gives me this thing that no human being would ever tell in an informal chat conversation with an agent in customer service. It's just really different. And then people are very good in chunking things, so they would say, I don't know, are you one of those, Would you write whole message in one single chat?

Dive (39:56.732)
You

Vitaly Friedman (40:19.468)
and then send it. Here we go. But AI, doesn't chunk. It's like, let me tell you the story about my life, and then I'll tell you something else. But these are going to be two huge chunks. And then there are a couple of things that you can scroll through. People are different. People see through this right away. So if you have an AI that is pretending to be human, this is the best way to erode trust and make sure that people never come back to it again, because then they're probably going to write something like, speak to human.

Dive (40:19.691)
no, I chunked everything.

Vitaly Friedman (40:49.134)
in the chat and wait for it to happen. And if you don't have this option, they're probably going to send an email to you whether you want it or not.

Dive (40:57.318)
Hmm. Anything else that designers should be considering if the goal is to maintain this trust in an AI experience?

Vitaly Friedman (41:08.766)
Well, would say the best way to get the trust is to provide accuracy. Unfortunately, we just can't do that really absolutely reliably with AI like we do with software, right? So I guess scoping would be very important there. so scoping is kind of get to the same idea as kind of gathering enough context. But what I mean by scoping, it's something like...

Let me maybe see if I can actually show it. I think that Luke also wrote about this at some point. Don't let me see. think it's like, I think he called it context chips. Let's see, not content management. I think maybe it was even that part. Yeah, so something like that, context chips, right? But basically, we want to make sure that people understand where they are.

Very often the problem is that they might be asking a question, but to get that notion of trust, they need to understand where the answer is coming from. Typically it's the internet, right? It's the internet. And the internet cannot be necessarily trusted. So if you want to elicit trust and build trust, we're gonna need to show sources. And it's actually also quite helpful to be able to indicate what is the domain or the scope

that is respected for that query that the person is submitting. So it could be not necessarily a file like it is over here. It could be like these little filters, like let's say experts with 20 years of experience or anything like that. And in fact, nothing is being displayed most of the time. We don't see any reference about what specifically was kind of explored or studied. It seems like it's almost random. Maybe it actually is. I'm not quite sure how everything is working under the hood in some of those AI engines.

But maybe it would be a good idea to say, OK, these are not just the sources of where it's coming from, but more global scope. For this query, we consider 279 pages from experts who seem to be credible and have this level of expertise and have at least this degree in, I don't know, whatever, in health care, in any kind of health care type thing. So anything like that could be quite helpful. And on the other hand,

Vitaly Friedman (43:31.842)
What I would also say is, needs to probably, probably the best way to build trust is to reflect back to people that they understood. And the way to do that is through kind of highlighting what we assume or what we believe in. Just to give you an example, ChetGPT and also everybody else as well at this point have memory, right? So if you go to customize ChetGPT, there are some things that you can say to AI about yourself.

I think it's kind of in preferences and settings. So is it personalized? Yes. So you can actually have memory. So you can basically reference saved memories and also reference chat history. You can also manage that. So basically, you can say, you know what, Georgia GBT, remember that I like carrots. Do you like carrots, Mike?

Dive (44:23.452)
They're okay.

Vitaly Friedman (44:24.684)
Hmm, that was not very exciting. All right, here we go. Remember that I like carrots? And then of course it does, it remembers it. So next time it will actually, if I ask something like, me a recipe for dinner, right? It might give you, here we go. Look at that, right there. I didn't even tell ggpd to do that, but now it knows, right? So that's nice, that's great.

Dive (44:43.974)
Look at that. There you go.

Vitaly Friedman (44:52.43)
But it can also tell me, maybe it could be like a batch right here. Vegan, carrots, or whatever else that I like, just to reflect back to me that I know you. This is where it's coming from. It doesn't have to be like text, oh, here is a vegan carrot for a cuisine recipe that is simple, flavorful, and satisfying. Maybe you don't have to write all of that. Just write me vegan, because you're vegan, carrot, because you like carrots, and whatever else. Just as an indicator, as a signal that it understands

Dive (45:04.195)
Interesting, yeah.

Dive (45:18.352)
Yeah.

Vitaly Friedman (45:22.286)
So it kind of explains why it's coming with this, right?

Dive (45:25.596)
Yeah, I like that too because then you could turn off carrot and you all of a sudden have a one click affordance instead of having to type actually I don't think I'm going to want to eat carrots tonight.

Vitaly Friedman (45:30.218)
Yeah, exactly. exactly. Exactly. So you can kind of build it up. Or maybe it could be a drop down, we can select something else. But instead, we're just dealing with stacks. And now if you want to say, I don't want carrots today, I do like carrots, don't remove carrots from my memory, but I don't want to have carrots today, that becomes a story. And you cannot just tweak and say, you know what, make it more, I don't know, more mushroomy. I don't even know what it means.

Dive (45:37.947)
Yeah.

Dive (45:51.13)
Mm-hmm.

Vitaly Friedman (45:59.532)
I want more mushrooms. Make it more mushroomy in a way. There is no way. There is no tweak in that. There is no button on that. And now it asks me a question. And then I have to go again and type.

Dive (46:04.23)
Yeah.

Dive (46:11.108)
And if you do want to iterate on it, you would probably go down this path that would lead you to eight full responses stacked vertically, which all of sudden becomes very difficult to parse where in a perfect world, I almost want like, okay, here's the ingredient list. And I want to be able to perform like item level interactions. maybe I would. Yeah, exactly. Or like even exploring things, maybe this isn't the perfect use case for spatial exploration, but I'm really, really in this interested in campus-based workflows right now.

Vitaly Friedman (46:18.806)
Yeah. Yes, yes.

Vitaly Friedman (46:27.852)
and maybe even to do this like a checkbox, right?

Vitaly Friedman (46:40.044)
Yep.

Dive (46:40.41)
And this would be a perfect example where I'm like, okay, this looks pretty good, but there's like this chunk. I don't, maybe I don't have these ingredients. Okay. Now let me just isolate that and iterate on like, okay, what can I do instead? And maybe I want to try three different things and then, okay, this is the one and I insert it back in rather than having this like really repetitive output over and over again.

Vitaly Friedman (46:50.785)
Absolutely.

Vitaly Friedman (46:56.844)
Yeah, so this kind of refinement journey, think that these are, they are the most painful ones because if you need to tweak now, well, you need to kind of see, okay, what else, what from this do I need or do I want or what do I not want? And then you say, maybe more like this, maybe more like that. And it's, this is a horrible input, more like this, more like that. Because I mean, you have to copy paste whatever it is that you like and say, I have this, I don't have that. This is, this is just waste of time.

Dive (47:02.545)
Yeah.

Dive (47:25.115)
Mm-hmm.

Vitaly Friedman (47:25.902)
It's just a waste of time. So we could actually have a more interactive experience here by breaking this down into some topics. mean, of course, it would be happening later because once the output is generated, it's generated token by token. So at this point when you're generating it, you don't know what's coming up and you don't know maybe necessarily what it's going to be like. But then you can actually do this sort of post-processing potentially and say, present it as this. Or maybe you could have this little button here saying to do this, make a to do list out of that or whatever.

Whenever it comes to a list, it could be presented this way. So those things really feel like, OK, give me a break. This is just little niceties, right? I think they compound and make a difference between people just spending a few minutes on a task and people spending 20 minutes on a task. That can make a difference, especially when you do some sort of profound research. And again, also this kind of

interaction or navigation between these turns. So if I ask something else now, I have two walls of text I need to go through every time. And if I find that, okay, this is not what I want at all, so let me go back. If you have like three or four of them, that becomes a story. But not here, right? Because if I go and I ask a follow-up question, let me just add it in here, something like specifically related to research in Iceland. Okay.

Greetings to everybody who's watching us from Iceland, by the way. Oh, there is 16 sources. Excellent. But now I can say, hey, here is a navigation between these two different queries. So I can also delete one if I don't find it relevant to me. So can say, hey, let me go back here. OK, no, no, let me go back here. Yeah, I love it. It's really, really nice. And then again, this option to delete.

Dive (49:02.972)
Hmm.

Dive (49:13.2)
Wow, such a little detail. It's great. Yeah, it's great.

Vitaly Friedman (49:21.022)
is super helpful too, so you just get what you need.

Dive (49:22.298)
Yeah. Yeah, because if you don't do something right or you get this wall of text that isn't as relevant as you thought it was going to be, it's now this permanent part of the record. It drives me crazy.

Vitaly Friedman (49:31.894)
Yeah. Or you have to restart the conversation all over again, kind of asking the same thing. So these are all just really kind of small things that do add up. Maybe one thing I would like to show, if that's OK. So this is Exa. Exa is also pretty cool. And I think you can see quite a few tools doing that, because there is a lot of different.

Dive (49:35.15)
Exactly. Yeah.

Dive (49:43.749)
Yeah, please.

Vitaly Friedman (49:54.094)
kind of interaction modes. mean, we spoke just about chat, right? But of course there is also voice and voice is usually very difficult to deal with in general. But there is also a way to present data in a slightly different way, like a data table, but maybe almost like a data grid. So there is websites here. And the websites here, you can actually look for things and kind of gives you this list, right? The reason why I wanted to show this is because it's actually really interesting of what it actually does. So if I took, let's say something like,

founding engineers at the AI startups based in Seattle, get me the technical strength and seniority. What I love about this is that it also takes the prompt and then it breaks it down into kind of almost like UI controls. So it says, okay, I'm going to break it into themes. So first of all, I to find founding engineers to the company developing AI products and services. That's all right. A company is classified as an AI startup. That's about right. Person is based in Seattle.

Seems to be right. And I can also add some other criteria here and say, ponding engineers, right? I don't know, any preference that I have? I have no idea what criteria to add here.

Dive (51:08.565)
You could proficient in React.

Vitaly Friedman (51:13.582)
Oh, here we go, proficient in React. All here we go. I can also exclude some things, which again, no AI allows you to do. So it's kind of like literary filtering, right? And you can say, oh, hold on for a moment, depending on what I'm looking for, gives me a way to add enrichments. So what else do you want to know from them? Is it just tech strength, maybe? Years of experience? Graduation date? Anything else that you find relevant? And how many results do you want? So then I start searching. Okay, here we go.

Dive (51:21.425)
Yeah.

Vitaly Friedman (51:44.878)
Don't tell me I don't have enough credits. This is the story of my life, by the way. Yeah, yeah, that's okay. Yes, sure, of course, beautiful. But basically what you get is you get a table. I need 330 more credits to create this website. That's disappointing. So it basically creates a table with all this information pulled out. And because I told it that I need 25 results, it will actually try to find as many sources as it can to give me 25 results.

Dive (51:47.484)
We'll just cut this right out.

Vitaly Friedman (52:14.478)
So I will get a spreadsheet with 25 results, and they all can be filtered with all the data for each of those things that I find relevant for me. So I can compare it, and I can sort by it. Why on earth don't we have an option to sort and filter results that we're getting from AI? Isn't it the most obvious thing ever? And I mean, I'm not coming across as probably the most grumpiest person ever, right? But those are...

Dive (52:41.308)
because you've done your research.

Vitaly Friedman (52:42.69)
Yeah, but there's a little, little things really that can tremendously improve experience tremendously. And they are things that we are used to in software, but for some reason they never really make it to AI. I'm not quite sure why.

Vitaly Friedman (52:59.308)
I'm sure.

Dive (53:01.57)
more questions maybe before I let you go. And I kind of want to zoom out a little bit. There's another design challenge that I've experienced as someone working on a product that involves a lot of AI, where you kind of have this spectrum on one end, you have the more disguised AI and everything's happening behind the scenes and on the other, you know, you're just slapping sparkle icons everywhere. So there's the spectrum and basically every designer has to figure out where do I fit onto that spectrum? What advice do you have for that?

Vitaly Friedman (53:02.712)
Sure, sure,

Dive (53:31.334)
person. Well, how are you thinking through that challenge?

Vitaly Friedman (53:32.322)
Yeah. So I have like, I don't know why, but this is like something that I also observe and this is something that we call Quiet AI versus Visible AI. So there are a few tools, like for example, Dovetail. Dovetail is a tool for researchers, which allows you to record sessions and finds insights and create reports and kind of, and all the good stuff that researchers need to do. And what was really surprising to me is that there is no sparkles there. None.

Basically, what you have is you take a close look at the user journey and you look at what people need to do. Well, they need to be able to record sessions. They need to do recruiting. Okay, maybe AI can help with that, right? They need to find some insights. Okay, so maybe AI can help with that. Maybe you also need to redact some sensitive information that people are providing. Well, AI can help with that. So you basically take a look at the existing journey, then you sprinkle a bit of AI all across it to either reduce frustrations,

or improve or speed up successes. And so that's the quality. It's kind of all indeed, as you're saying, happening under the hood. But on the other hand, we have these experiences where it's kind of almost feels like AI first. And I'm a little bit allergic to AI first in general, because I feel like, well, it's like saying JavaScript first, or I don't know, ships first, and containers first, or anything.

Dive (54:50.012)
You

Vitaly Friedman (54:55.224)
Technology is here to serve and to help people get somewhere. So if anything, we should not be that obsessed about AI, but to be absolutely obsessed about humans because they are the ones who are kind of using that technology in the end. So we really need to do a lot of research to understand what do they do with AI, not what we do with AI. I mean, we can do things with AI. I mean, we are technologists, if you like. But we need to be obsessed about how people use that thing.

For me, the really important thing is not to say AI first, but maybe AI second, not AI last, but we need to think about what is it that AI is good for in our product that we're delivering, right? So what value does it bring? And then we see where people struggle in getting that value and where we can actually boost that value even further. If there is a thing, a certain area, let's say, where people lose a lot of time, they waste a lot of

going back and forth and maybe they don't know what they want necessarily so we need to guide them somewhere, right? Well, maybe I can help there and that's great, but it's the thing, it's not the value generator, it's sort of a path to the value that AI provides. It has an incredible opportunity, we just have a feeling that we haven't really unpacked it properly yet, right? And so personally I would say I would look at user needs, I would look at what people, where people struggle.

Dive (56:04.593)
Yeah.

Vitaly Friedman (56:21.59)
and then boost it all up with a bit of AI to see that we can maybe really help people there. But also on that journey, think it's important that we allow people to reduce that interaction cost that we were speaking about before, articulating what is it that they want and so on, and also helping them in the cases where they are struggling with the output and they want to refine it. Because AI doesn't come for free. It feels like it's magical, it can do everything for us.

It comes with a tremendous cost. mean, there are many, many different layers from interaction costs and fixing errors costs to compute costs to energy costs. It's like now technology comes for free. We just need to be aware of that. And so when somebody submits a prompt, right, I want that prompt to be almost perfect, almost ideal. So I know everything that I need to know to really generate something meaningful. Otherwise it's waste of time and energy and everything in between. So.

Personally, and I'm not trying to be difficult, but I guess I am, I would probably go with the quiet AI, quiet or quiet AI direction rather than loud AI. Also, which is very funny, there was a research done by a thing by Normal Nielsen Group. And what they discovered is that actually when people see AI as a label or badge somewhere, it's not necessarily a good thing because people are not looking for AI features. They're looking for features that work.

Dive (57:23.941)
You

Dive (57:48.39)
Yeah.

Vitaly Friedman (57:49.698)
happened to be AI or not. But it's not necessarily something that customers really appreciate. Like, they have AI feature now. Where is that AI feature? And also, it can even have this opposite effect where, because it's AI, it's maybe untrustworthy. Maybe it's hallucinating. Maybe it does that and does that. So I would always run a test to say, OK, this is an AI feature or AI powered, and this is just a feature.

or a product, right? And see what works better. I would not be surprised if there would be no difference at all. Or if anything, yeah.

Dive (58:19.568)
Mm-hmm.

Dive (58:25.436)
I can already f-

I can already feel it in like, I can already feel it for myself where I just assume that I'm going to be upsold when I click on an AI feature. And it, it happens so many times I see the little sparkle. I'm like, Oh, that's interesting. We click and it's like, you have to upgrade to our next plan. And I'm like, man, I'm so tired of this.

Vitaly Friedman (58:37.006)
Mm.

Vitaly Friedman (58:43.938)
Yeah, but you know what? This is interesting, because I think that this is an issue that lot of people have, because they realize that even whatever tool you're using, people are running at the limits of the credits very quickly, much faster than we think, because they think, like, I'm just going to go further and just play a bit more and play a bit more, experiment a bit more. And before you know it, you're running out of credits, and then you either pay, and usually, it's not, I mean, it can be affordable, but it can be very expensive, Not everybody wants to pay for a pro, like,

Dive (58:55.195)
Mm-hmm.

Vitaly Friedman (59:13.678)
plan $200 a month or so, even if it produces incredible deep research and whatever, that's expensive. I mean, that's really expensive. And so when you're hitting limitations of a tier, this is it. This is the end of the journey. And the goal is, for most products, I think that a lot of companies are realizing that now, we need to get people to some success within the credit plan that they have.

And that does not mean give them the free form textbooks to do whatever they want. Because then they hit that limit very, very quickly. We need to guide them to make that prompt small, and accurate, and concise, so they don't prompt more. They should prompt less, but better. So we need to give them some success in the first session before they hit the limits of the free tier. But if they just keep going, keep going, keep going, keep going.

Dive (59:45.85)
Yeah.

Vitaly Friedman (01:00:07.616)
it might be either very expensive for the company because they're just using too many credits, right? Or they will be hitting the limitations too fast. And then there is no value either way.

Dive (01:00:17.05)
I had a contractor who was working on my house and every day he would say the same thing. He'd say slow is smooth and smooth is fast. I'm like, that's, it kind of applies here.

Vitaly Friedman (01:00:25.312)
I like that. Yeah. Yeah, I think so. Always listen to your contractors. Very good people.

Dive (01:00:30.352)
I always listen to the God directors. Before I let you go one final question, and I kind of want to just look a little bit further into the future and get inside your brain a bit. You're obviously thinking about all of these different UX principles and how they evolve and these emergent behaviors that we're seeing as much as basically anybody that I know. So when you kind of look in terms of where this is all headed, maybe it's more agentic behaviors. Maybe it's

just different ways of interfacing with AI. What are some of the things that you have your eye on right now that you're particularly excited to see?

Vitaly Friedman (01:01:05.546)
Yes, I think that there's lot of excitement about agents, but in practice, as of now at least, there is very little reliability in that space. Also, because agents always come with some guardrails that they need to establish. That means permissions, that means you need to have some sort of approval layers and things like that. I mean, nothing comes for free, right? It can be quite challenging to put together in the first place.

But what I really believe in, and I think that's, you know, if somebody is watching this 20 years, I'll be thinking, what the hell were they thinking back then? I think that we will probably not end up seeing a lot of prompt engineering guides anymore. I think that in the end, it will be just a part of UI. I think that at this point, like all these little things will be just natural. We're just doing, like some people would say, I think it maybe was a head of design for Flexity who said that.

In many ways, AI can be perceived very much like fancy new thing that will be very much like autocomplete now, just everywhere. A little bit of that, a little bit of this, a little bit of AI here, a little bit of that here, but not really properly advertised as the big new thing. I mean, I don't see a lot of people saying, oh, this is autocomplete first experience. Now we're talking. This is magical. It's just a thing that we are used to, and this is it. We just need to clearly label AI as AI.

Dive (01:02:20.378)
Yeah. Yeah.

Vitaly Friedman (01:02:30.574)
So people understand that okay, this is like a that thing that can do some things but maybe not always accurately and and that's okay, right and they will find use cases for that and I think that this is probably on the level of UI all the things that I probably mentioned today I'm pretty sure that a couple of years from now. It will be like a different world altogether I mean, I'm pretty sure about that. But on the other hand when I look at the task that AI can do kind of perform away can help I think

One significant shift at least to me is that we're probably moving to the world where we are becoming less tactical and more strategic in many ways. That means that, you know, not a day passes by without somebody on the fringes of the internet telling us that we're going to be replaced by AI. And if not, AI that's going to replace it, then people who know and understand and get AI will replace us. And I think I disagree because I think that there is an enormous value that humans

bring to the table. And I think not only in terms of like critical thinking, emotional intelligence and so on that goes without saying, but to me, there must be somebody who has a vision about where the hell it's going. So I don't want to have, don't, I don't believe maybe for now, maybe I'm just naive, but I don't see products being designed and developed by AI to serve people at the best way possible. I mean, to be able to create this connection, almost like a

strong emotional connection with the product, I must, maybe I'm just really naive, but I must see people working on it who put a lot of thought into what my experience is like. And I'm not sure if any AI can out-care and out-love this attention to details that people bring to the table. And so in the end, what I think is kind of us humans, right, moving away from the work that we're doing, yes, it will change and it has already changed and it will be shifting further. I have no questions about that.

But that only means that what we're doing will be different. We'll be just orchestrating those AI experiences in some way or the other, maybe with agents, maybe with agents who have sub-agents and whatever. But somebody must be guiding and orchestrating and kind of creating this experience for people. Because AI is very good at creating experiences, but I'm not sure if it's creating experiences for people who... I want to see people who kind of come to a website who...

Vitaly Friedman (01:04:56.406)
and AI product and say, this is amazing, I absolutely love it, I want to use it every day, that they feel like extremely passionate about it and they really, really want to use it because they fell in love with this interface because of how it understands people's needs, it understands what people care about, it understands when to say things in certain way and what not, when to adapt a particular tone and voice. And maybe I can do that.

But I'm not trying to be like one of those people saying, no, AI, forget about AI. It's not important. We are the people. But I think that there is an enormous amount of value that we bring to the table. We just shouldn't forget that. And what I'm expecting, and that's a very long answer to your question, is that we need to see that there are a lot of things that AI is very good at. There are a lot of things that humans are very good at. What I want to see are wonderful.

human first experiences that happen to have some AI components in them. That's what I want to see, right? Where you kind of have the marriage of both. I think we need both.

Dive (01:05:59.004)
Yeah, I couldn't agree more and really, really appreciate you coming on and getting super specific about things too. I mean, this was just fun to see how you are interpreting the space and what you're paying attention to and what you're studying. So really, really grateful you took time to share it with us today.

Vitaly Friedman (01:06:08.92)
Yeah.

Vitaly Friedman (01:06:16.75)
Oh no, thank you so much for having me. I can be here tomorrow and the day after tomorrow. That's not a problem at all. think that's okay. That's okay. I think the main point for me is that there is a enormous amount of value in finding those little details because I think that they can really break and make an interface or make an experience. It's like when those things really come together, they really do compound and then you have a very different experience. I mean, I think like...

Dive (01:06:20.892)
Careful I'll take you up on it.

Vitaly Friedman (01:06:44.386)
The very first AI product that I fell in love with is actually this one, which is Consensus. I probably would use it even if I didn't find anything meaningful for me there. It's just a great AI experience. I would love to see more of that.

Dive (01:06:49.212)
Yeah.

Dive (01:07:00.368)
I mean, I hope that's what this episode does for people is even gives a little bit of a finer lens that designers can use to interpret some of the AI experience that they're playing with. And also to see the tiny subtle details and opportunities that they can take advantage to make these products something that are truly usable and not still just riding the wave of these new technological capabilities.

Vitaly Friedman (01:07:23.296)
sure for sure well let's let's wait and see I guess maybe once we watch this like 20 years later so thinking well they had interfaces back then that's interesting

Dive (01:07:27.044)
You

Dive (01:07:33.308)
I love it. This has been fun. Thanks for tally.

Vitaly Friedman (01:07:38.53)
Thank you so much for having me.

