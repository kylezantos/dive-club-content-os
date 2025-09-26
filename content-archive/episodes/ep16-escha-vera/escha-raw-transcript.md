Dive (00:00.191)
perplexity journey. Because, like, if I recall, you didn't actually even know that you'd be working on Comet, maybe? Okay, okay. So like, talk to me about, like, you're deciding to join, you don't even know, like, just where does the story start, basically, right before that line of your hand at the keys to Comet? If you want to share that context, and then we can just kind of see where it takes us.

Escha (00:07.726)
Right.

Escha (00:17.432)
Mm-hmm.

Escha (00:22.924)
Yeah, so I left Descript and I kind of felt like maybe my career is over. I spent so, so long on one product that I kind of left feeling like I did myself a disservice by doing that. And I felt unhirable for whatever reason, low, just low self-esteem, I guess.

Dive (00:29.672)
Gah!

Dive (00:44.338)
Yeah, so not deserved to. Descript was like one of the most cutting edge products ever.

Escha (00:49.806)
So I spent like a year just talking to CEOs and other companies, startups, like trying to figure out what I wanted to do, if I even wanted to stay in the AI space or if I kind of felt like it was time to distance myself and just go back to the regular grind. And I didn't really find anything that felt good. Like either I got bad answers to questions I had about

or just like the way that they were approaching the integration of AI into their tooling or whatever it was, or they didn't have answers and that made me uncomfortable. So I know Soleo, I know him early on from Descript. I reached out to him and asked him if there was any companies that he knew that was kind of looking for someone or someone that might be a good fit for me.

And that's why I got connected with Daylight as well. But he just sent me an intro email with Henry of like, hey, founding designer to founding designer, y'all should know each other. And that was like a year before I joined. So we just had some casual correspondence. At the time, Henry was focused on building up the brand team. And I said, hey, whenever you're...

focused on product, hit me up, let me know. And so about a year later, after kind of spinning the wheels on daylight stuff, working on the OS and working on motif, reached back out to Henry. He was ready and looking for product designers. And I got all the right answers to the questions that I wanted surrounding AI, how it's used, what it's...

just like all of these gritty details that I care about as a designer who's like putting my name behind the products that these companies are pushing out. And I asked Henry, hey, like, do know what I'll be working on? Like, is there any research I should be doing? Like, is there anything I can get started on, like, ahead of my actual start date? And he was like, yeah, maybe, maybe some desktop stuff. And I was like, okay, well.

Escha (03:13.944)
I don't know what that means. That doesn't really mean anything. I've been doing this stuff forever. So it's, it's whatever. I guess I'm going in blind. and the day I joined was the day they announced Comet. So I didn't even know about Comet until like, I woke up, started working, saw the announcement on Twitter and I was like, that's really interesting. and then my first meeting with Henry, he was like, Hey, so I started like,

Dive (03:34.6)
You

Escha (03:41.837)
very early stages of this browser thing. But do you just want the keys? Do you just want the keys to own this? So that was very cool. It was very, I mean, just so honored to be handed a product like that. And first day, just having the keys to own product. So that's kinda how that started.

Dive (03:48.262)
That's so cool.

Dive (04:11.432)
Alright, so I definitely want to dig into the journey, but I want to return to something you talked about a couple times. And I'd like to know, like, what were those kind of gritty details about Perplexity's approach to AI that made you feel comfortable joining?

Escha (04:28.666)
I mean, part of it is just like what, what's happening with users data, like how are these models being trained? How does perplexity go about choosing what models get put into the system? And like even further, like how does the system actually read those models? How does it, how does it work? Like something I didn't know, but it's kind of interesting is that with the model selector,

People think that that's actually choosing the model to like run your query through. But really all that's doing is choosing the model for the summary. Like whatever text that it spits out is the answer. The model is choosing what's generating that actual answer. All of the processing actually goes through all models.

Dive (05:22.152)
interesting.

Escha (05:23.148)
So Perplexity has kind of done the work to decide and figure out like benchmarks, like our own internal benchmarks of like what models are the best at certain things and just putting in classifiers that when you are prompting, it knows what models to run everything through and it runs them through either in parallel or sequentially before actually spitting out your answer. So that the model selector actually doesn't have as much.

Dive (05:48.774)
Hmm.

Escha (05:51.767)
impact as people think it does. And so just like asking those questions, like how does this, how does any of this shit work? And having like confident answers given back to me of like, okay, we don't, know, that when you submit a query, obviously, like specifically with comment.

Again, classifiers are used. It'll pick out like what data it needs in order to give you a good answer. It'll pull that from the browser. Like everything is client-side. Like we don't actually store any of your data. It'll take that, it'll hit a server once and then delete it immediately. So we don't actually store any of that stuff. like the fact that it even hits a server once is...

It's a security risk. It's concerning to some people. It's a reason enough to not use a product. And it was just comforting hearing that like, okay, well really the end goal is like a year from now, two years from now, six months from now, who knows technology moves so fast when models are efficient enough to be able to run on the machine. like you don't even have to hit a server at all. And at that point, literally everything will be client side and everything will be protected.

which is like kind of the polar opposite approach of like open AI. Like with open AI, everything is a server call. And so that just gave me a lot of confidence and like, okay, well, the sort of trajectory of the company, the sort of like the ethics around data and how AI is used for

for research or anything that perplexity can do, just gave me lot of comfort versus something like mid-journey, which I love mid-journey, but there's so many unanswered questions with mid-journey that no one really knows and they don't really talk about. And if you ask the questions, you don't really get the answers. And for me, that's reason enough to not really want to contribute.

Escha (08:11.68)
unless I get those answers.

Dive (08:16.464)
I want to return back to some of the AI stuff, but maybe we could just continue on with the journey a little bit. You use the phrase being handed the keys. It's a pretty big deal. What the heck was that first month like? And that's a heck of a, that's a big time ramp up process. Like where do you even start as a new designer, new team, and yeah, you've now inherited this massive product that has this whole hype cycle attached to it on Twitter.

Escha (08:40.792)
So from the outside, looking at Perplexity, it's a very polished product. mean, has some quirks, it some bugs, there's some UX things that could be better, but overall, it feels not like 20 designers are designing it. It feels like a small team. There's a lot of just continuity and consistency. So my first instinct was, all right, I'm gonna go through Figma files and find this.

Design system, I'm gonna find the pieces that I could use to just start riffing on ideas and quickly found out there is no design system, at least in Figma. Maybe this is commonplace, but I've never worked anywhere that operated like this, but code is law. The design system is in the code. A lot of the designers here are actually contributing directly to front end.

Dive (09:16.1)
You

Escha (09:36.633)
So that was interesting, just kind of realizing, okay, there are Figma files, but everyone's kind of just making their own components as they need to fulfill a design. everyone has taste and just like common sense and they can pull from what is on the web, but it's really like screenshotting and then like making the component based on what's on the web. And that's probably fine for...

complexity core because it's a web-based product. Comet has overlap between C++ code and the web. And it's two different teams. And the web team kind of has what they need and they have the sort of infrastructure they need to be able to build out front-end UIs. But the C++ team didn't have anything. They needed mockups. They needed pixel perfection. They needed prototypes.

And so I started by just making a design system. I made it for myself because I needed something to quickly iterate on the C++ and like the core browser Chrome pieces. And then team kind of saw that and was like, hey, this is sick. Like we could totally use this for perplexity. So that kind of exploded the scope of that from a Comet design system to a perplexity design system that kind of has

Dive (10:57.265)
wow.

Escha (11:04.91)
continuity between the two, they're literally the same system.

Dive (11:08.91)
And is this Figma? Is this code? Is it both? Okay.

Escha (11:11.928)
both. it was majority of like my work was was in Figma, working primarily with Champore, who's kind of one of the all stars here on front end and just design and taste in general. So I worked a lot with him on the front end side and making like implementing changes to the web based design system.

So just like making small improvements, but it was a really cool process because it was just me and Shampori, just making the calls and pushing the code. And I found that like working at perplexities kind of like that, like consistently. Like if you, most of the time when I ask what if, like I come to the table with an idea or I have feedback on something like,

What if we did it this way? What if perplexity or Comet could do this? And most of the time the answer is, cool, like do it. just, just like, you know, find, find the time, find the bandwidth, make sure you're managing yourself, but just, just do it. There's, you'll, you'll hear the words like phrase a lot at perplexity of just high autonomy, high ownership, high responsibility, high impact.

And it couldn't be more true. Like the design team in general is just given so much trust to not just propose a design solution, but to actually help implement the thing. So like on the design system side, it wasn't like coming to the team or coming to some stakeholders being like, is it okay if we change this? It was just like, do it.

Dive (13:06.979)
Hmm.

Escha (13:07.106)
have confidence that you know it won't break anything or like do your due diligence in making sure that it's right or getting feedback from Champoria, the smaller team. But it was really kind of on us to make those decisions and see it through.

Dive (13:24.909)
How far did you go into the design system direction? Especially as I'm sure there's probably some pressure to ship real screens quickly given the amount of surface area that you have to take on. So I'm interested in that intersection point. Like where's the sweet spot where the design system is contributing toward the output and tempo of what you're building versus over-architecting something getting kind of lost in the sauce a bit.

Escha (13:53.581)
Yeah, I'll try and answer that. think like the most of like what is in the design system in Figma is just the core atoms of components. A text component that's used inside of a button component, list item components which have an icon component, know, just like building up the atoms of this core component so that we don't actually have to componentize the bigger pieces. Those can be.

just left alone and be flexible and like up to the discretion of the designer to make it work. Just establishing like principles and the logic for like padding and spacing depending on the surface area. So there's like surface area logic that's just baked into auto layout within Figma. So it was really just the whole point was setting up.

components that can just any designer can easily use without having to remake it every time. Having a source of truth for that instead of having to dig around design files to try and find something. And just providing the guidance for how to put a design piece together. Like for me personally, I put padding into the components themselves so that when you're laying out the design, you don't have to worry too much about

like the distance between a piece of text and, you know, a button below it, you're, going to get that padding for free baked into that component. And it's going to be eight, you know, it's going to be divisibles of eight, sometimes four or two for like a micro unit, but eight, 16, 24, 32, 40, kind of up the scale. But we don't really have to even think about that. It's just baked into the system.

Dive (15:34.262)
Mm-hmm.

Escha (15:45.805)
And so obviously doing that work on the coding and the engineering end as well. And just kind of like making sure that tokens are named the same and really doing our best to make it a one-to-one so that even a new engineer could come in, look at it at a design in Figma, being able to inspect it enough to see what components are being used, what color variables are being used, and then use.

the design system on their end to put it together and they don't even have to worry about padding. They get all that for free. But there's also another piece of that, which is like prototyping code. I'm personally still trying to figure that out. Like what's the best way to do that? I've tried so many prototyping tools and like they're all okay. Most of them are geared towards mobile interactions.

Dive (16:33.61)
Yeah, same.

Escha (16:44.462)
pretty much all of them are okay for like transitions or like States, but aren't great for like complex user flows in a desktop environment. and so what I've found kind of just was working the best right now is Claude cursor and Claude.

Dive (17:06.283)
Hmm. Can you go a little bit deeper on that part of the process for you?

Escha (17:10.542)
Still figuring it out. It's still like relatively new for me. I've done like experimentation on my own, but I've never actually used it like for my day job. But it's like so far the process is putting together key screens in Figma using Claude or Chriser to kind of describe the thing I'm trying to prototype using those screenshots to actually build the initial front end.

It's not perfect, but it's either close enough or it is like, it's easy enough for me to go in and fix the HTML or the CSS or something to actually get that right. And that's been really helpful for like flows that require text input or dealing with a suggestion list as a, type ahead and like the steps and stages after that.

Like also just figuring out like quirky ways of getting things closer for the engineers. Like for instance, the onboarding flow or the landing screen for onboarding within Comet with the sort of rotating planet. That should probably be a 3D object. And it will be eventually, but.

didn't press press for time, press for resources. I ended up using Perplexity Labs to make that. I basically just took a texture, like a branded texture for the planets that we had, made a version of it that was seamless, used Perplexity Labs to just describe like, I want a orb in the middle of the screen on a white background.

add a button to be able to like swap out the texture, add some controls so I could play with lighting, and add a button to export a 360 degree video. And that was that. And I just exported that video and cropped it. And that's literally what ended up being put into production. And I did that, it took like two minutes. So just like figuring out ways to like...

Escha (19:31.375)
It's kind of hacky, I guess, but it works and I'm constantly learning what the boundaries and what the limits are for these tools. Like kind of working within the tool to figure out where the edges are and doing my best to try and push that. But once I feel like I've kind of dropped that or built the skill into how to communicate with the tool to get what I want.

then it's like, okay, well, what other tools can I put into this workflow to actually do even more than what I'm limited to within this one thing?

Dive (20:06.816)
That's the key word that I keep coming back to is workflow. Like for the first time in a long time, it does feel like there are many different tools that we can pull from and stitch together into this workflow to create an artifact that previously, I think about those like planets that you made, they're beautiful, right? That would have clearly sat outside of my box of potential deliverables as a designer a couple of years ago. There's just no way, I wouldn't.

be messing with that type of artifact and yet it was really special, right? Like the amount of times that I saw that celebrated on Twitter in the week that you released it, I lost track quite quickly. And it's so cool to hear that that was you just saying, you what if, you know, and just hacking something together.

Escha (20:53.198)
It's also cool because I can't take full credit for making that texture. I kind of took what we were working with and edited it and manipulated it in order to work for that context. it's kind of one of the beautiful things about Perplexity, again, I'm probably going to say this a lot, is the brand team is so good. And it's all just the design team. The separation between the brand team and the product team is a

Dive (21:13.362)
Yeah, it helps.

Escha (21:22.178)
you know, a waist high wall. There's so much collaboration and communication between the two teams. Like I'm contributing a lot on the brand side, even though I'm just a product designer. But having the opportunity to work with brand designers in that way, instead of it just being like a handoff, hey, we need some marketing materials, like, know, pinging the brand Slack and be like, I'm working on this thing. Does anyone have any assets? Does anyone have any ideas? Does anyone have bandwidth?

Dive (21:42.526)
Mm-hmm.

Escha (21:51.15)
to jam with me on this.

Dive (21:53.779)
Yeah, I mean that's the dream. I finished interviewing Phi and was immediately like, man, I wonder what it'd be like to have a Phi to work with, because I'm sure that I would look like a better designer as a result.

Escha (22:05.536)
It's amazing. First hand, it's incredible. is a godsend.

Dive (22:14.771)
Yeah, yeah. Let's talk about the onboarding a little bit. That was one of the things that I wanted to dig into because it's so creative, art direction, everything. Obviously the brand team played a role too, but talk to me about that process. Like where did you even start thinking about what is the best way to onboard users? What types of feelings do I wanna evoke? How'd you land? Where you landed?

Escha (22:41.602)
Yeah, I mean, it was no different than any other typical onboarding, like design process at the start, just figuring out like, what's the key information that we need to get from the user in order to make their first experience when they actually get into the browser as good as possible? So that's things like importing profiles from other browsers, like having starting with a, with history is gonna make your

your answers so much better, because it has all of that context.

See what else is even in onboarding? I mean, the initial setup, like, what do you want to name this profile? Pick a theme color. Setting the browser as default, which is kind of a tall order and a high ask. The reality is it's a really lightweight action, but it's not perceived as one. But it makes a huge difference in just the retention and the overall quality of your experience trying a new browser.

And so just getting those in place, making sure that we don't have too many screens, the more screens you add, the more kind of drop off you have. Although it might be a little bit different with a browser. Like if you've gone out of your way to like download the browser, you could probably get away with a few extra steps, but I really want to keep it like as minimal as possible. And then once we had that, it's like, okay, well, this is kind of boring. Like I can, you know, play with the styling a little bit, but it's still just...

It feels like product onboarding. And I really wanted it to feel like something special. yeah, yeah, yeah. Or like the, just the idea to put music in. Like that wouldn't have happened if I didn't just make it happen. The intro sequence with the animation and the logo reveal, like that.

Dive (24:22.683)
Yeah, it felt like an unboxing moment for me.

Escha (24:44.002)
I wanted it to feel like when you start up a Nintendo 64 game, just like an old school video game when you start up and you get the production credits before the title screen. I think I was like low key, like subconsciously inspired by like Genshin Impact. I've never actually played Genshin Impact, but while I was working on Komet and onboarding,

my girlfriend was often like on the couch just playing Genshin Impact. And I could just like hear the sounds and the soundtrack or even like someone pointed this out after the fact, but like the title screen for Genshin Impact is kinda evocative in the comic onboarding. And I see it now, now that it was pointed out, but that was just like a subconscious thing. I think I was mostly largely just inspired by video games and...

that experience and kind of wanting to see more of that in product design. And onboarding was the perfect way to do that, whether that's with imagery or animations or music and sound.

Dive (25:53.403)
Yeah, the music was a big deal for me. Like I've been designing for a long time and I've never added music to a flow as a deliverable, but you felt it. Like it definitely transformed the entire initial experience for me.

Escha (26:06.67)
think one of the only products that in recent memory that has something like that is Bandcamp's login screen on iOS. They have this like, when you're on the login screen, they have this like really cute, Incredibles-esque sounding, just theme music. And it's been there for years. Like no one ever talks about it. I've never seen anything else like it. But it was just this like really neat moment.

It turned what was otherwise just very standard boring login screen into something that had a little bit of delight. It had like a distinct identity. And I would just love to see more of that. And I think for me, like I'm passionate about music because I've just been, I know so many producers. I've been in the music scene for so long. I used to do like shows and SF with

an ex-girlfriend of mine. And I have a label. just like, I don't want to shoehorn all of that in unless we want to talk about it, but I work with producers, just as a passion project. It's kind of what I spend my income on is paying producers to let me work with them and release their music. And so I have a couple of producers that I've just known.

Dive (27:13.904)
cool.

Escha (27:34.721)
since I was a kid almost. And we just have such a good working relationship that like the comet theme was basically me going to one of my friends and being like, hey, make something nostalgic. Like that was the prompt for the comet intro theme. And the title of that track is

Escha (28:03.374)
I forgot what it is. Hold on. It's a good title. Let me find it really quick.

Dive (28:06.447)
Yeah, you're good, you're good.

Escha (28:19.31)
So the title of that track is Waking Up Before Everyone Else at the Sleepover and the Wii is still on.

Dive (28:26.107)
I love that. I love that.

Escha (28:29.888)
And it fits that so well. the producer's name is Nesso. I have to give him a shout out. He's highly slept on. He's so talented. He can nail any genre. Like a lot of how I work with him is like coming to him with a couple of different tracks or ideas or something or a seed or like a sample of something or an idea of like a genre blend. Like something that I think could work, but I've never heard it before.

Dive (28:32.43)
Yeah.

Dive (28:38.114)
Yeah, we'll put it in the show notes.

Escha (29:00.07)
And he's just, he's the one who's going to nail it first try. And he's just so open to trying new things. So I kind of just work with him naturally just because we enjoy doing it. And it's been awesome being able to like pull him into perplexity stuff a little bit, like all of the sound effects for, for the, the Comet game, all done by Ness.

some of the tracks for the live stream are either originals from Nessow or just like from some of the other producers I work with. But that's where Suno comes in. Suno like is something that like I tried initially when it came out and then I kind of put it off and never touched it again. And then I kind of like was curious and just kind of picked it back up saying what else is new. And it's incredible. Like not enough people are talking about how good it is. And it's good for

Dive (29:38.894)
Yeah, helps.

Dive (29:51.862)
It's so good.

I haven't... No, no, you're good, you're good, keep going.

Escha (29:57.323)
sorry.

It's good for specific things that no one is talking about, like remixing vocals or like taking splice vocals, which are often like not really what you want to use, but it's what's available to you. Like using that as an input through Suno to actually remix those vocals or change the lyrics or like turning a vocal melody into an instrument.

if you have a flow or a cadence and some vocal that you like, it's so easy to turn that into a saxophone. Or just genre blend. What does it sound like to mix metalcore with drum and bass? Add some jazz in there. And if you work with it, you kind of... It's the same with any other tool. The more you work with it, the more skill you build in how to communicate with it in order to get what you're envisioning.

And yeah, so like I've been now using Suno to just as a scratch pad of ideas and then sending that to Nesso and being like, Hey, is there anything here? And oftentimes like I'll send Nesso the stems because I can export stems from Suno and then he'll either like use some of those pieces or just create his own version of that. And then send something back to me and it's just like just some back and forth there.

Dive (31:07.428)
Hmm.

Escha (31:28.654)
And we are kind of like working on an EP right now that's like entirely the result of me generating music, using samples from him, sending it to him, and then he's just making something from scratch inspired by that. Something that like we would have otherwise never made if we weren't experimenting with this type of workflow.

Dive (31:52.986)
And it sounds like you have music background, but a lot of people listening probably don't. So you know, it's just this mechanism that you can use to express yourself through audio that you otherwise would have no right or ability to do, you know? And I think it just goes back to what we were talking about earlier, where we're seeing this expansion of the box of what a designer can potentially bring to the table and what it means to truly own the experience, right? Like you brought in the video of the planets.

Escha (32:20.238)
Mm-hmm.

Dive (32:22.711)
you're bringing in this music here. And like all of that is so tied to the feeling that you were able to evoke with Comet in the first like 20 seconds. And yet it's not in Figma, it's not in pixels, you know, but you designed it and so cool, so cool.

Escha (32:37.442)
it.

Dive (32:44.299)
Let's, if you have something else to say, for it.

Escha (32:47.79)
was going say we could talk about the invites a little bit if you want. I don't know how deep you want to go on there, but there is something interesting there.

Dive (32:55.425)
Yeah, yeah, let's talk about the... I'll cue it up here. Can we talk about the invites next? I know that was something that you owned end-to-ends. I've seen a bunch of them on Twitter. What's the story there?

Escha (33:09.922)
Yeah, so we decided to do an invite only rollout initially, just to stress test everything to make sure nothing broke, didn't get overloaded. Also just to get our opportunity to get early feedback from users. Although I feel like...

It's interesting because that feedback is obviously coming from early adopters and not like the lay person or really who the target audience is for a comment. But yeah, so we decided we were going to do invites. We needed an invite system. The first thing was like first pass QR code. That's the easiest thing, but it's kind of boring. Like everyone has done QR codes. There's been some clever things, but it

Dive (33:38.381)
Yeah.

Escha (34:00.023)
It still just doesn't feel special. And I really wanted to make it feel special. I wanted everyone to be excited about the invite itself. And so I played around a bit and we, like a couple of weeks prior we had launched Perplexify Me, which was just an experiment, like an in-house, like what if idea that turned into a thing.

which was just the ability to upload a profile picture and have it be converted into a style that is within Proplexity's brand.

Dive (34:40.639)
I did it on me, it was cool. I liked the output a lot.

Escha (34:43.182)
So that was cool, like working with, I didn't actually work on that, but the fruits of it were cool. But that was like a process of engineering and working with a brand team fee, working on prompts for like both the literal prompt and the inputs that like helped create that style so that it's consistent between every generation. And I loved that.

And I thought there was an opportunity to do something there with the invites. So I basically just kind of took some brand assets that we currently have, like either made by Fee or the people on the brand team or like the creative investors who are using Mid Journey and sharing style codes. So I kind of just spent like a day going through artifacts that we already had, going through style codes, going in Mid Journey and just

like throwing stuff at the wall, trying to like figure out what could it invite even be if we made it generative. Tried a couple of things that either like didn't end up being scalable, because this that was also important. But I eventually through like cutting up pieces of either existing artifacts or stuff that I like use that as an input within mid journey and eventually got

a style of something that I thought was good within brand and was scalable. Took those, brought them into Photoshop, edited them, like edited the, just the composition, the layering, played with blend modes to get like a certain effect that I wanted that I couldn't quite get out of mid-journey or like didn't come to mind when I was in the generative iteration part.

used those, re-imputed those into midternee, got just a subset of what I thought would have been good fodder for training data, used Civet AI to actually make a model. So I played around there, made a dozen or so models, picked like three that I thought were good or like kind of paired well with each other, and then used FAL AI.

Escha (37:05.154)
to actually set up the flow for the generations. So with FAL, you can just take a model code that you generated with Sivit. I ended up using three. You can like blend multiple models together. So I picked out three models, played around with the weights of like how I wanted those models to be weighted against each other, started playing with prompts, kind of like pulled from what I was using in mid-journey.

but editing it a little bit, just again, just learning how FAL works and how to talk with it and found a prompt that worked there. Played a lot with other parameters around like just how many times it'll run through the model in order to generate the image. There's like a slew of parameters that you can play with. I spent like a day playing with those, just seeing what outputs I got.

and making sure that it was scalable over time. And then I went back to the prompt and just found pieces that could either be variable-ized, like color, and then just created some color variables that could be swapped out. Like if blue is mentioned, maybe it's turquoise or whatever else in another version of that prompt. Additions and subtractions, like including black hole or...

motion, like some have more motion than others. Some are kind of more liquidified, some are more cloudy. So like just building a stretch, prompt that has pieces that can be swapped or variableized and then just set that up on the, on the engineering side so that it runs through those at runtime and just randomizes them. And so you, I mean, I stress test this and you can get like up to like

10,000 generations and they are all unique, but stay within a level of variance that feels distinguishable and like identifiable as a comet invite.

Escha (39:19.128)
So yeah, I don't.

Dive (39:19.936)
How much of this workflow did you have any level of familiarity with before? Like, had you used these tools before? Had you done large scale generation before? I mean, you just even listed off a bunch of tools that I'm not even familiar with. how'd you figure all this out?

Escha (39:38.951)
I mean, I've been doing just experimentation on my own for a couple of years now, like on Twitter, I'm kind of, I'm like an advocate for, for AI, but I try to be a good example of like how to use it ethically or like just creatively like, Hey, you can use this and this and this and put them together and use them in different like order within your, within your workflow or whatever. But so I had some familiarity with.

like training my own models, not specifically with Civet. I had used other tools in the past. I had used stable diffusion flux. So there's a number of options that I had either tried once or a couple of times, or just had been familiar with by name as those had come up in my feed or whatever. I had never used FAL or Civet prior to doing this.

just kind of was curious and gave it a try. And it ended up being the one that worked.

Dive (40:46.613)
Cool. I'm inspired. I think, again, this idea of workflows and figuring out ways and tools to unlock new capabilities feels kind of like this whole new frontier for being a designer. So really, really cool to hear this backstory.

Escha (41:01.754)
It's definitely one of the more exciting pieces about the whole thing in general, like not even just perplexity, but just in general, designers using AI. That's what's getting me excited is realizing that it's looking at AI or like the, looking at the outputs not as outputs, but as throughputs, like either

Dive (41:26.876)
Hmm. I love that.

Escha (41:29.646)
putting it into another tool and then putting it back in or just constant feedback loop of reiterating or remixing an output. Like anything I've ever shared is the result of constant just regurgitating that flow like dozens of times. Anything I've ever shared has hundreds of parents that led to that result.

Dive (42:00.948)
Okay, that's a I'm gonna I'm gonna I'm gonna switch we could go down this forever. It's so cool Like I was making the real-time decision of like how deep do I want to go here?

I wanna zoom out for a second and talk a little bit more broadly about the product strategy behind Comet, the role that design played in that. It seems like there was quite a bit about Teonomi. You're probably making thousands of micro decisions, but were there other core strategy decisions that you were wrestling with or maybe even like an inflection point in the project that kind of changed where you ended up landing that we could drill into to understand a little bit about how you as a designer wrestle with

ambiguity and kind of work your way through some of the more complex parts of the design process.

Escha (42:49.484)
Yeah, I'll try.

I think the one that's top of mind at least was just establishing like who are we building this for? Like who is the user? Like everyone needs a browser. Everyone uses browsers, but who is Comet for specifically? Why would you use Comet? And so establishing that like...

Comet is for the lay person, at least initially. It's kind of a strategy thing. It's as wide a net as possible. Comet is for your parents. It's for the person who gets a new laptop and they just install Google Chrome without thinking about it because they've never really tried anything else or they're not someone who's coming from Arc or Dia or like they might be coming from Edge or Chrome.

and so that, that influenced a lot of the early decision making, on just what does comment look like? part of it was it's Chromium. It's a Chromium build as most browsers are these days. You're either Chromium or you're Firefox. And they're, it's like basically impossible to make your own at this point.

Apple is an outlier with Safari. So it's Chromium. So we got a lot of Chrome and Chromium stuff for free. And then it was decisions on like, okay, well, what do we change? Obviously, I think there's a ton of room for improvement across the board, but like, how far do we wanna go in making it novel versus familiar?

Escha (44:43.314)
And a lot of these early revs of the early days of the product are leaning far more on the familiar side. So we'll get feedback that, hey, I was expecting Comet to be something crazy or something that I've never seen before. But I installed it, and it just kind of looks like Chrome. For better or for worse, some people are like, it's like.

Why isn't it different? And other people are like, Hey, this is great. I don't have to learn something new. Everything is where I, you know, expect it to be, or, that helps kind of push the AI use cases and the assistant a little bit more as being the one thing to really focus in on or try, or, you know, there's a bit of a learning curve and like even figuring out like

what I would use the assistant for, what can the assistant even do? So by making the Chrome and the browser experience a little bit more on the familiar end, we have more bandwidth from the user to be able to focus in on those things instead of doing what Arc did. I I use Arc still. It's hard to move away from sidebar tabs. Like that changed my life fundamentally.

Escha (46:08.202)
But, and we're, I mean, gonna get there eventually. it's kind of like, Arc started that, but Arc also did a bunch of other stuff that kind of scared users away. It kind of hurt their ability to grow their market share. Some things felt a little bit arbitrary. Some things, again, I think are brilliant, but it adds cognitive.

Dive (46:24.06)
Totally.

Escha (46:37.428)
load to the user when they're just trying to try a new browser that I think we were trying to avoid initially. Funnily enough, going back to like when I was talking about the decision to make it a rollout with InSpy only and that meaning that our initial users are probably going to be power users or people who are tech adopters.

like majority of feedback is you need vertical tabs, like yeah, yeah. But it'll be interesting. And we're already starting to see as we opened up invites, so like we're getting more lay people in as time has gone on and we're ramping up for general launch, that feedback is starting to dwindle a little bit just because there's people who have never used vertical tabs and so they don't understand.

Dive (47:08.772)
Yeah, there's a dissonance there.

Escha (47:33.782)
like the value of that. So they're not really asking for it. But it is interesting now, if you look at any other browser, any other like

Dive (47:35.442)
Mm-hmm.

Escha (47:42.99)
I don't know, browser that you should probably consider using offers vertical tabs at this point. I think Chrome is the only one that doesn't, ironically.

Dive (47:54.246)
Hmm. Maybe we could drill into... do you have more you want to try on this? Go for it.

Escha (47:56.233)
yeah. No, I was going to say sorry for rambling. I don't know if that answered your question.

Dive (48:02.45)
No, it's perfect. It's perfect. It's perfect. Maybe we could drill into just the AI piece then. So a lot of the decisions that you are making as far as the Chrome go, they're affording you the ability to pursue at least an element of novelty there. So could we talk a little bit about some of the design directions? What were you exploring and how did you land and how did you land where? Hmm. I'm going to ask that.

How'd you arrive at what ultimately shipped?

Escha (48:35.106)
Yeah.

Escha (48:41.26)
I think like a lot of this is the result of an excellent team. Like there's an agent's team on the engineering side and they're coming from places where they have so much experience and that already that like a lot of those decisions or the way that technology works was not really up to me. It was up to me to make it usable.

and to help find the use cases to then provide feedback to improve the agent to be able to do those things. I mean, there's like the surface area question on like, where does this live? What does it look like? How do I engage with it?

and kind of approached it as a hidden extension. It's just a sidebar. There were explorations of that being a floating window. Potentially we'll still explore doing some of that stuff even still like as an option so you can kind of undock it from the sidebar. But the sidebar was just the easiest, quickest thing to do. And then there were deeper questions of like, is it tab-based or is it

window-based. Like, if I'm going between tabs, does the assistant follow me or does it refresh and is it kind of like a new assistant per tab? If we did the window-based stuff, it's like, okay, well, now we got to make sure that clearing out the thread is intuitive and makes sense and is something that you would do because

what I found is that people wouldn't clear the thread. And with the way perplexity works in a thread, that's where the context builds. And so if you start asking questions that are totally unrelated to that thread, it'll start getting confused because it'll feed in that stuff. so like starting a new thread is important in perplexity. think like there's opportunities to like change that the way that it works so that that's less important, but that was something that we had to tackle.

Escha (51:02.836)
wanting like wanting to make it easy to like compare between a Windows laptop and a MacBook. Like I should be able to go to Windows and go to apple.com, go to the pages for those laptops and have comment tell me like what's the best value? Like which one should I actually buy? And so one way of doing that is by making it window based. So I could open up Apple.

ask the question, switch over to Windows, ask the same question. It has the context that I was asking this from Apple. And then that happens. The other way of doing that where it's tab based, it's like, okay, well, in order to do that, then we actually gotta be able to mention tabs, or we gotta make the agent smart enough to look at your open tabs so that you don't even have to like be explicit or verbose in your question.

or whatever you're trying to get out of it, the combination of classifiers and inference and also just knowing to check your history, check all tabs that are open, decide what's relevant and give you the right thing. So that was a bit of just trial and error, like having a gut feeling that it should be window-based, trying it out, realizing that it has pitfalls, it's...

kind of confusing sometimes and ended up going towards tab-based, which was not my first instinct. Like, that's not what I thought I wanted until we tried it and then realized that there's other ways, whether that's functionally how the agent works or introducing mechanisms like mentioning tabs to be able to make those things work. But also trying to think like, like I see

Comet or the browser as the first step towards an OS or an agentic OS. Like it would be so cool if Comet could also look at what's on your computer or act on other like first party apps that are installed on your computer, not just web apps that you have open in a tab. Kind of gets into the, the, and the,

Escha (53:28.29)
the MCP realm where I could sling Slack and Notion and Comet together all using their native apps to enable different workflows. Another thing too is if it's tab-based, that means you're doing a query on that tab, whether it's contextual or whatever, but you could only...

like that query lives within the context of that tab. So also exploring like, okay, well, what if we had like a command center? What if we had like a surface area that's just focused on the agent that doesn't have to live within a tab? It can be its own thing or I could schedule queries or run many queries at once and be able to manage those.

string them together, still being able to add mention tabs or do anything, engage with stuff within the browser itself, but not being locked down to like, okay, I've got to have a tab open on a webpage in order to use the assistant.

Dive (54:43.018)
Every time I talk to someone that's designing browsers that always comes up the temptation or the desire to have like the personal homepage that kind of does everything you know it's like it's always there and then you always end up maybe somewhere slightly different I want to reply I want to go back to something you talked about where this

I want to go back to the switch between like window based to tab based and how that ended up going against the initial instinct. Were there any other places in the design process where you ultimately advocated for something that was a little bit different than what you originally thought?

Escha (55:34.466)
Well...

Escha (55:37.985)
That's certainly like one of the biggest ones that like I low key feel bad about, you know, it's like the kind of thing where like, I thought through this thing, I came out with this opinion and I was able to back that up with why, and I felt confident that like, this is the thing to try. And then it ended up not being the right answer. And I was like, my God, like I totally fucked that up. But like, try not to.

Dive (56:00.427)
Yeah.

Dive (56:06.445)
I'm like three days from having a very similar thing where I sent us down like a two week rabbit hole that was just in retrospect wrong. And I totally thought it was right. So I get it. It's like one of the hardest parts about being a designer.

Escha (56:20.768)
Another surface area and something you just touched on or mentioned is just the new tab page. Should we even have a new tab page? What are the benefits of actually having a surface area show up when you hit new tab versus Arc, which is a spotlight model? There is no new tab page. It's just search.

have done explorations on both of those, still doing that, still open to how far can we push this and what is the north star here. But ultimately decided, let's start with a new tab page that gives us a branded surface area. It gives us the opportunity to introduce widgets, have some branded really cool widgets, like a tri-assistant widget, which just like...

does a random agent inquiry, just to like a quick one-click way to get you to a magic moment, to maybe plant a seed of like, this browser can do something I didn't think was even possible. Or the Comet game, which is kind of like the offline equivalent for Comet, but having an entry point for that. Recent sites, like that's pretty valuable.

an entry point into like perplexity proper and your whole perplexity account in your library. So like, it just made sense to start with a new tab page for all of those reasons, but probably, honestly, probably doesn't make sense in the long run. Like there's, there's probably a better solution. And so just like not, not.

trying to feel too bad that we have a new tab page right now, and even though we don't really want one, or like...

Escha (58:25.624)
haven't quite landed on what is the best alternative.

Dive (58:32.971)
There's kind of this spectrum of decisions that I have in my brain where on one hand you have some of the lower level visual component details that it sounds like you're kind of just owning. You feel the autonomy to just make that call, ship it, and we'll figure it out. And then on the other end, there's these really meaty strategic decisions like windows versus tabs for the agent. And then there's this messy middle ground in between. And I'd kind of like you to help me make sense of that messy middle ground a little bit.

specifically as someone who's on a new team, you know? Like you're still kind of even figuring out how to work with these people a little bit. So how do you think about the right level of collaboration versus just making the call? When do you strategically bring people along for the ride, loop in key stakeholders, and what does that look like in your practice?

Escha (59:24.748)
Yeah. So for me, initially, it was constant. I was constantly bugging everyone. But it was, was like a, it was just part of the onboarding process for a new team. Like just trying to figure out where things are. If we have a pre-existing, you know, pattern or a solution for this particular problem, have we thought about this? Just trying to get a sense of like how the team thinks.

Dive (59:32.916)
I bet.

Escha (59:54.263)
Like, what are their answers to this thing? And just like, why did they answer it that way? And learning so that over time, I don't have to bug them. I can be confident that like, I know what they would say, or I know what their approach would be.

And so it's kind of gotten less and less, at least for me personally, as I've matured within the team and have a better sense of answers to those questions that might come up.

Escha (01:00:33.312)
It's also maybe a bit of an anomaly because I was the only one on comment. Like there's Gunner who's like on iOS and mobile and he's like the king of mobile. There's Champore who's like owns most of the agent and like core perplexity answer stuff.

people who are tackling enterprise, people who are more around spaces. So everyone's like kind of has their specialty in a surface area that's quite broad. And I started and I was the only one on Comet. At this point, we've hired two extra designers to help me. So that's been great. So we have someone on mobile helping me with Comet, so iOS and Android.

And just someone just started to also help me with desktop stuff So it's it's kind of like opening the doors again, like I'm pinging them all the time like hey Tell me everything I did wrong like like help me Second guess all of these decisions While also trying to give them all of the context of like how we got to where we are and why we made those decisions and where we still want to improve and

Dive (01:01:36.383)
Nice.

Escha (01:02:01.647)
Now we're having a lot more syncs, a lot more jam sessions, which is fun and very cool to see and very exciting. And it's helping ease some of my anxiety of like...

feeling like I have to make a decision or the right decision. I am a designer. I suffer from decision paralysis. I wear the same thing every day because I don't want to deal with that in my real life because it's my job. yeah, it's, it's again, just to recap, guess for me personally, a lot of it just initially comes from wanting to understand.

how the team thinks and how people operate and what the overall alignment is on a direction for the product. And once I feel like I've grok that, it's less about asking those questions and more about just throwing stuff in Slack for feedback. If you have time, if you have bandwidth, take a look at this, let me know what you think. If not, don't worry about it.

Dive (01:03:12.431)
Yeah, it's going out the door. Well, it's an impressive feat to own that many decisions across that large of a surface area. You do have a pretty awesome background. know, first designer at Descript, right? Is that correct? Yeah. So you had the first designer at Descript. You've

Escha (01:03:32.728)
Mm-hmm.

Dive (01:03:37.021)
You mentioned like motif and daylight. So it's not your first rodeo in terms of everyday tools. So are there lessons learned or maybe principles that you find yourself pulling from based off of your experience designing these other tools while working on Comet?

Escha (01:03:58.319)
Hopefully. Let me think about that for a sec. Like, the answer is definitely. I just don't know what the best answer to that is.

Dive (01:03:59.465)
You

Dive (01:04:07.409)
Yeah, you're fine. You're You can take, I know it's tough question. You can take a minute if you need it. I think this is like one of the main things I want to just tap into is you obviously have thought a lot about this.

Escha (01:04:26.774)
Yeah, I mean there's there's really so much like a lot of them are like small things Trying to think like if there's anything meaty

Escha (01:04:45.363)
Escha (01:04:54.03)
Maybe I'll speak to like two things and then like maybe think about it a little bit more. like, one is I've just been, I've been doing design systems my entire career. I kind of like got introduced to the concept of design systems when I was working at a UX firm. My main client was Microsoft. This was in like 2008, 2009. So like I helped establish the design language for Metro.

Dive (01:04:58.098)
Sure, sure, sure, sure.

Escha (01:05:23.074)
what like turned into Windows 8 or Windows Phone or the Xbox, the Surface tablet, I kind of like was able to work with those teams to establish a design system that can live across all platforms. And there was a huge, at Microsoft, like the huge thing was accessibility. And so that was just ingrained in me.

Dive (01:05:23.4)
Bye.

Escha (01:05:49.743)
early on in my career of like how important that is and how important design systems are or systems design is. And at the time they were like design systems were PDFs. Like they were not things that you could use. They were things that you would reference. And everywhere I've been since then, I've mostly been a lone wolf. I've been like, I was the only designer at Descript until like

I was at OpenTable before that and I was working on the restaurant product. I was the only designer on the restaurant product. The whole rest of the team was on the website or brand or like the iOS app. Everyone wanted to work on the iOS consumer app. It was the shiny thing when like iOS 7 was first introduced. But I was like, no, I want to work on the thing that makes the company money. I want to work on like the hard problem.

But I ended up being a lone wolf. I was like the only designer on that product. And then kind of took it to detour, pre-descript was the same thing. Then we kind of like sold assets to Bose and kind of turned that into a descript, spun it off as its own tool, because descriptor was an internal tool that we made for detour. So I've just been alone for so long.

that I didn't actually even have designers to riff on. I was like working with a CEO in the way that I would work with designers. And so I just gained a lot of muscle in being able to like make those decisions or set myself up with a framework that can scale no matter what like the product is or what the surface area is.

And that's proven like really valuable for me. Like I mentioned like in the beginning of this, like when I stayed at Descript for so long that I felt like I did myself a disservice that I wasn't, I didn't like grow. There was a period of time where I felt stagnant being in the same place for so long. Just kind of growing within a industry area within a product, but not like growing as a designer. But.

Escha (01:08:15.656)
after that, like post that, joining Perplexity, joining a design team, realizing that like I was just building skill and muscle that whole time. That's kind of like what enabled me to hit the ground running with Comet on my own for the first couple of months.

Dive (01:08:39.417)
Is there an example of a framework that you would then apply to make a decision or understand how to think through something on your own? Like, can we make that practical for something for somebody? Because I think that's a pretty interesting thing you just said.

Escha (01:08:54.648)
Yeah, can you ask that in different words maybe?

Dive (01:08:56.901)
Yeah, yeah, yeah, so, so, so, you talked about this idea of equipping yourself with a framework to operate against as somebody who doesn't have a bunch of designers to constantly ping for ideas or just helping to process something. Can you talk a little bit or maybe point at an example of a framework that you've used or what that looks like in process in practice as the lone wolf designer?

Escha (01:09:21.582)
Yeah. Yeah. I don't think any of these are going to be like, like mind opening or anything. But they might be helpful or like, just for like younger or newer designers, this might be helpful. I don't know. I'll give it a shot. So one is just like spacing.

like realizing that there's a lot of power and value in divisibles of eight. So if you're working with a type system or you're laying out a page and you're working on like layout or editorial or interface design where you're mixing in like text and buttons and inputs and other pieces to make a design,

Early in my career, it was just all vibes. It was just all feel. But over time, kind of experimenting and having happy accidents with eight, not 12, not 10, but eight. And like occasionally using four and two as like a micro unit when needed, but sticking with eight and 16 and 32 for the most part, for the majority of things where I'm.

either working with text sizes or padding. And just, I don't know that I would come up with like a really great example of like why that's, why divisibles VAD are so good. You just end up having a lot of happy accidents as you're designing something where you get a result that looks right without you trying to really.

do that. Like if you're dealing with complex or very like stacked and layered interfaces that are very dense, or you're working with text within a button and that button is within an input and that input has icons, if you're sticking with these rules, you don't have to think too much about it. And when you're playing with

Escha (01:11:49.909)
layouts and removing things and throwing things and reordering things just to like throw stuff at the wall and like Feel it out as you're designing it It just works I don't know how else to say it other than it just works and you end up getting a lot for free and you end up with a lot of happy accidents that you might not have landed on other things are just like Basic good general best practices for

interfaces or for UX. Like if you have a right click or a list menu or you you have an input that opens up a drop down when it's just a list. Like how many do you show? You could have it be the full height. You could have it only show you know seven and a half, eight and a half list items. General ballpark best practice just to make it feel digestible. But make sure you cut off that last half.

so that it is clear to the user that there's more below the fold of that menu so you can still scroll within that list. Choosing whether or not you use icons in menu items. I do, I try to use them sparingly, because like the default, like what you might wanna do is just put icons on everything. But when you like have them everywhere,

Dive (01:13:02.702)
Do you?

Escha (01:13:18.09)
in a product, every service area, in every context menu, every list item as an icon, they totally lose their meaning. They lose the impact they have to help navigate the interface. They just end up adding more cognitive load than is worth. So then it's just a matter of like, okay, being a little bit more disciplined about that. Only adding icons if they either make sense or if you have a large menu.

And there are certain list items that you think are more important or have higher priority for a certain workflow or whatever context it's in.

and just making those decisions on when to use an icon and when not so that in the broader scheme, helps make the ones with icons stand out. It doesn't matter what the icon is. Just adding visual variance that helps with digesting an interface.

Dive (01:14:19.108)
Do have any frameworks or rules of thumb or something like that as it relates to integrating AI into a tool? Because you've been thinking about that a lot too. mean, Descript is doing a ton with AI way before it was cool. So I'm curious if anything comes to mind on

Escha (01:14:28.11)
Thank you.

Escha (01:14:34.062)
Yeah, so not a lot of people even realize it, but dscript has been an AI tool under the hood from the ground up from the beginning. We just never marketed it like that. In 2015, AI was not really a house called acronym. It didn't mean the same thing it does mean today. It wasn't important that the tool was AI. It was important that the tool had features that worked and that offered value.

Escha (01:15:02.606)
And so one thing was just the decision to not market it like an AI tool. We didn't need a blast that everywhere. We didn't need a jump on a bandwagon. We just needed to show the value in the tool. But internally in the tool itself, it's like, okay, instead of labeling features as AI, just put the feature in a place that makes sense or use AI to surface the feature contextually as a suggestion.

at a time when it is actually makes sense to surface to the user. So that helps with just helping a user learn how to use a tool, like help them discover features that are either buried or they would have had to like take time to go through every menu in order to discover. You can actually surface that to them at a moment when it makes sense to surface.

I think like an example of the former would be like Notion, like when Notion first started doing AI, was like the purple stars were like features in Notion were labeled as AI features. And now those are just, it's commonplace. Like it's no longer this like new concept that you have to grok. It's just part of the tool and the way it works. And it doesn't matter that it's AI or not.

Dive (01:16:18.583)
Mm-hmm.

Escha (01:16:29.91)
On the feature side though, there's things like...

like filler word removal in Descript. Like just call it filler word removal. Don't call it AI something, green screen. Even things that are inherent to the way that the tool works and not necessarily a feature that the user can engage with. Like in Descript, if you are making edits and you make a clip, it actually does a micro crossfade between those clips so that you don't get a pop in between that.

normally if you're a sound engineer you would go through and make every you would make that that edit but Descript kind of just does it on its own and we're not loud about it you don't need to know that it's happening you just know that hey that edit sounds good and I didn't have to do a bunch of work to make it sound good if you create a gap or you regenerate audio it uses the surrounding audio to generate

So like early days, you needed like a voice model and you would spend like 30 minutes training a voice model and it would always use that voice model. But the downside was that model was trained in a certain recording environment with a certain, you know, like it had a certain style and now you have to stick to.

Dive (01:17:52.577)
Yeah, I did that on an old mic. I was like, man, this ceiling is capped.

Escha (01:17:56.397)
Yeah, yeah, yeah. Yeah, yeah, you have to like stick to that style or it it stops the return on investment kind of hits a wall. So we move towards like, just use the surrounding audio. You don't need a model. You just need at least like five seconds of audio on either end of your cut or your regeneration. And that just don't have to spend the time explaining model training. Don't have to like,

There was so much work put into Descript on like the security and just making sure that the tool can't be abused. Only you can train a voice model for yourself. Only you can generate audio of your own voice. You can't regenerate audio of someone else unless you get permission from that person. And in order to get permission, it basically you email or send the user something.

they see what you're trying to edit so they can verify that like, you can edit this thing. And then you have to verify that it's you by reading a randomly generated script. And then we would check that audio with the audio of what's trying to be generated to make sure that it's the same person. But we certainly didn't need to do a lot of that work if we're just using the surrounding audio.

Escha (01:19:25.696)
In general, higher level, stepping back. AI and tooling is interesting because it's so early. We're, figuring out the patterns. Like the, the, the out the gate, like first thing that we did was chat. Like support style, like chat interfaces and prompts. Both I think are problematic. They're less than ideal for being usable.

They're an engineering approach. It's a headless UI. It's so powerful, but it requires so much upfront to learn how to use it and what's possible. And it leads to a blinking cursor problem for new users and laypeople. It's just like, cool, I got this blank input. What the hell do I do with this? Like, what can I even do with this? And so with Descript,

prompting and chat was treated like a second class citizen. was custom instructions instead of prompt what you want. It was like, do you really know what you want? Cool, go for it. Otherwise, here's an interface. Here's sliders and dropdowns and a description to help you choose what you want. But just like putting all of these features like,

Generate clips, for instance, as an example of a feature within T-Script. You can take a podcast and you can generate clips for social media. You could do that with a prompt. You could just tell it to do that. But what we ended up doing was building an interface. So feature is clip, generate clips, make clips. When you open that up, it shows you just like, okay, how long do you want these clips to be? Choose a slider. How many clips do you want?

Is there a certain topic that you want to focus on? What's the format? Like, is this for Instagram or TikTok or Twitter? Like there are questions that we can get answers to upfront, just with a general user interface that actually on the backend starts to build that prompt. But the user doesn't need to know what the prompt is. It's just either like it's secret sauce and we don't want you to know, or it's just, it's overkill.

Escha (01:21:53.207)
It's information you don't really need to know if you're not interested in learning how to be a prompt engineer. It just happens in the background under the hood. And if you want, you can customize it. You can hit the custom instructions button and add your own prompt on top of that. But that in general was the approach with Descript was productizing the AI, whether it's by feature and not calling it AI.

or if it is AI, not leading with a prompt or chat, but leading with getting information that we need through an interface to actually give you a good result.

Dive (01:22:35.072)
How applicable is that approach to designing the product going to be for Comma, especially as you all have laid the foundation for a truly agentic world that also accounts for an infinitely larger spectrum of possibilities because you're not just editing something, you're doing literally anything in a browser. So can you talk a little bit about some of the challenges or thinking behind this agentic future and what the future of

Escha (01:22:44.321)
Yeah.

Escha (01:22:50.946)
Mm-hmm.

Dive (01:23:04.179)
What future interfaces look like as you're designing this more agentic world?

Escha (01:23:09.42)
Yeah. So one is just the problem of discovery and like.

education on what Comet can do or what Comet can do for you, like personally and uniquely for you.

And so one approach to that is just a query library. Like we've got a set of dummy queries or like just basic queries that everyone has that we know will work. And the idea is maybe those plant seeds of ideas. Like you read this query in the library, you're browsing it, you see that it falls under a category of like email or whatever. And just using that as a mechanism to plant seeds of what Comet can do.

Then there's another layer of that, which is personalized queries. Actually, if you import your browser data or you have, you've used Comet and you have a history, you have bookmarks, we've kind of like, we're able to generate personalized queries for you that are specific and unique to you as another way of just helping plant the seeds of ideas. Like all of these are gonna work. You can just click the,

try and comment button and it'll work or you could hit save and save it as a shortcut if it's something that you would like see yourself doing repeatedly. But I've often just found it useful as a springboard of like, wow, shit, I didn't know comic could do that. I don't want this query specifically, but let me edit it. Like let me save it and then edit that shortcut and now I've got my own thing. Future version to that could be.

Dive (01:24:48.434)
Yeah.

Escha (01:25:00.14)
being able to share those queries, making your Comet query profile public so people could like see that and learn from. So that's one piece on like the discoverability.

Escha (01:25:18.456)
then there's usability in terms of.

Escha (01:25:25.194)
actually being in the product in real time capturing you at that moment. So we can do that with like zero suggests when you click into the Omnibox or the assistant input, we know what site you're on. We already know like we have a good idea of what makes sense to do on like a major domain for instance. Like eventually all of this will just be AI and inferred and generated. But to start like a good fair amount of it is just hard coded like we did the work.

to figure out what are popular domains, what are popular things to do on those domains, put those in zero suggests. So when you're on Notion and you click on the input, you've got a series of like suggestions that are specific to Notion that may or may not be relevant to what you're trying to do at that moment, but will get better over time at inferring that. depending on whether you have an empty document or a document that's filled, a document with spreadsheets in it, depending on the actions that you just took.

Dive (01:26:00.338)
Okay.

Escha (01:26:23.406)
prior to that. There's a lot that we could do with AI to infer what might be the next step, what workflow are you doing to suggest an action that Comet can do. Then there's like follow-ups. Like if you have a complex query or something that you want to do that's more complex, designing the agent in a way that's not just submit query, get answer, but actually submit query, see the browser working.

See the agent of what it's thinking, how it's learning in a website, how it's learning how to use that website. And then if it gets stuck or it needs a follow-up or something, pausing the agent, prompting that. You need to edit your credit card info. We need your approval to send this email before it just sends automatically. Put your final stamp on it.

or just suggesting follow-ups. Like, hey, you did this thing. There's another query, like it's similar to a zero suggest, but it's actually like a follow-up suggest.

Escha (01:27:37.912)
Lost my train of thought, but

Dive (01:27:39.397)
No, I have a smile listening to you talk because there's like an endless sea of design explorations in this world that you're describing and yet it trickles down to a comically small amount of unique UI.

Escha (01:27:58.684)
There was something else I was gonna mention and I can't think of it right now.

Dive (01:28:02.597)
You're good. We can chill for a second or if you remember it at any point we can always go back too.

Escha (01:28:11.15)
Yeah, there's like

Escha (01:28:25.102)
I don't know actually, I might not actually even be allowed to talk about it.

Dive (01:28:28.317)
Yeah, kind of, anytime we look more future-facing, I understand that that's often the answer. So, quick pause. I want to be respectful of time. I'm gonna, I a wrap up question that we can just jump to. Anything that we haven't talked about that you want to get onto the record. Otherwise we've a ton of ground, obviously.

Escha (01:29:03.342)
The, we don't have to talk about this, but there is something I tend to want to speak to, and this is less about perplexity, but more about AI in general, using it as a creative tool. Trying to be an advocate for AI online, trying to field the vitriol and the hatred.

but also trying to set a good example of how to use something or how something can be done or just.

spreading the, yeah, Yeah.

Dive (01:29:42.319)
Let me just tee you up. I'll tee you up. I'll tee you up. I'll just pause. Let's just end there. You want to just have that? I'll just give you a generic toss up and we can ride off into the sunset on that. Okay, cool. do it. Tip of the tongue, teeth in the lips. What I want to say.

Okay, well, we've covered a lot of ground. I appreciate you getting into the weeds of what you're thinking about as someone who's not only designing AI experiences, but really experimenting and tinkering with all of these tools. So maybe before I let you go, is there anything else that you think designers should be thinking about more when it comes to AI and the role that it plays in our practice?

Escha (01:30:25.954)
Yeah, I think.

I guess one of it is.

like being open and curious to use AI or figure out creative ways of using AI in your day-to-day, in your flows for a particular project, whatever it may be. Another side of that is how to choose what tools you use and how you use them. Like being mindful of the impact that AI has, whether that's environmentally or just

ethically, like image generation is a very hot topic. There's this kind of like this, it's interesting seeing like the stark contrast between engineers who use AI and designers who use AI and artists. Like those are three different communities and they all are very vocal on AI and ethics. And so I encourage in,

try to be sensitive to those things. I kind of try to be an advocate for AI while also trying to set the best example of how to use it. Whether it's like things that are obvious that I just believe in or things that I've uncovered or I tried and it happened to work. I've never seen anyone talk about it or do it that way before.

Escha (01:32:01.199)
Like having many followers on Twitter is not fun. It sucks. I just get a ton of just vitriol and hatred and pushback. But a lot of it is either misguided or misunderstood or just like the snowball is so big that it is hard to fight against that in any meaningful way.

Dive (01:32:30.906)
Yeah.

Escha (01:32:31.247)
And so trying to figure out how to do that.

Most people think, you just typed something. You just typed what you wanted and hit go and you got what you wanted. Either slot machine mechanic or you just ordered from a menu. And sure, AI can be that, but it doesn't have to be. It's not inherently that. AI is not inherently that limiting. It's actually so open-ended.

A lot of what I do is back and forth between Figma, Photoshop, at least like in image generation or art stuff. Like it's a back and forth between traditional tools and mid-journey as an example. Using my own art as inputs, using my own art as fodder for a model, using images from that model as inputs. Taking that, the output of that.

and just continuing to iterate on that and remix that. Take that output, put it in as another input along with two other inputs. Like really not just sticking to type words, hit go, but doing a bunch of what you would normally do as an artist or a creative and then using that to get variance on something.

Maybe it's a hit, maybe it's a miss. Maybe it's, you you might spend time iterating and not get anything, but sometimes you're gonna get a happy accident. Sometimes you're gonna get something that's like, hey, that's actually a really cool idea. I didn't think of doing that. Let me go back now and like do something and I might do something in a different way. But like using AI as a springboard for ideas, using AI as a communicative tool,

Dive (01:34:10.648)
Yeah.

Escha (01:34:30.912)
and less like.

as a tool to get around or avoid doing work. It's not about how little can you do, it's about how much more can you do because of AI as a tool within your workflow, whether it's at the beginning, the middle, the end. It's so open-ended and flexible and becoming increasingly even more with the introduction of MCP as a concept.

Dive (01:34:39.601)
I love that.

Dive (01:34:46.51)
Yeah.

Escha (01:35:04.878)
that I just find really exciting and trying to like teach people or show people the light that like.

Everyone hated Photoshop too. Like it was very controversial. Like Photoshop was in the news 30 years ago because of how controversial it was to move a horse from a bottom of a hill up to the top of the hill next to a tree to make a good format for a book cover. Like there was new segments on that because it was just so radical of an idea. Like, you're manipulating this photo. That's so.

That's so wrong. So while I feel like there's totally valid arguments against AI, there's valid concerns that I don't think we talk enough about or we don't address well enough directly head on. But I also think that a lot of those arguments, they are continuously getting more and more outdated as the technology gets better, as...

these models get smaller as they get quicker as you know, like a lot of stuff that the arguments against AI two years ago, three years ago are either no longer relevant or just less relevant. Yeah, yeah. So yeah, I just, I think and I truly believe that there is.

Dive (01:36:30.592)
Yeah, and they're fading, for sure.

Escha (01:36:41.736)
great power and opportunity in using AI ethically for good purpose and solves good problems that.

Escha (01:36:56.494)
I hope people are a little bit more mindful of whether they're deciding how they feel about AI, doing more research on it. Like I encourage everyone to do your own research. Be curious enough. Don't just listen to what you see on Twitter. don't fall into consensus.

And if you are using AI, just be mindful about the impact it has. Just the technology itself or how you're using it might have. Keep ethics and morals in mind. I think all of that is important. And it's important just for the longevity and the future of this tool. Like there will be bad actors and we need to hold bad actors accountable. It's not the technology that's the problem and it's not everybody that's the problem.

It's just, it's a garden that is ripe for abuse. companies that are implementing AI aren't mindful enough to be able to prevent those things or, I don't know, the floodgates are open, it's not going away. We have to live with it. And I'm just trying to do my best to guide the ship.

I ultimately decided to stay in AI and not back away from it in terms of my design career in the industry because I felt a moral obligation to be part of moving that forward in a direction that made me feel comfortable. ultimately couldn't live with exiting the scene and watching it go down a path that...

I wasn't comfortable with that I knew that I could have had an impact on.

Dive (01:38:50.923)
Well, Asha, I find it very inspiring. mean, for what it's worth, I think you did a really good job of articulating that difference and some of my own frustrations in seeing even the narrative around AI and what it looks like to use the tool as a slot machine, which kind of almost replaces the need for art in lot of ways, versus using the tools as an artist and tapping into that creativity and raising the ceiling. And you're doing

Escha (01:39:11.564)
Is it? Is it?

Dive (01:39:19.157)
You're exemplifying that so well. So I really appreciate you coming on today and giving us a little behind the scenes and sharing some of the workflows and what you're experimenting with. And I can genuinely say that I am a big fan of your work, both with Comet and Descript and everything. So thanks for the time.

Escha (01:39:37.624)
Thank you. Thank you so much. Appreciate it.

