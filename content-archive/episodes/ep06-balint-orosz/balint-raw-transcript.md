Ridd (00:00.014)
leaving people kind of just the context for why craft? How did this happen? What's the origin story that you share with people?

Balint Orosz (00:12.615)
Yeah, know, I think every, you know, engineer, know, person using computers always has this, you know, dream of creating a productivity tool they use every day. And I was no different. I think for me, this became a really exciting opportunity as, you know, I had a company which was acquired by another company, which was a lot bigger company called Skyscanner. This wasn't 2014. And, you know, this company had 10 offices across the globe.

which also meant that product engineering and my team was really much across the globe. And in my day-to-day work, this meant I needed to do a lot of asynchronous work. And back in the time, nowadays it's totally normal. We do everything in Slack, everybody's remote. But at that time, that was quite weird because usually everybody was at the office and you could do all of this. But then I realized I need to use email for everything, right? For short notes, for explaining long things.

And eventually you realize that it's really, really hard to get deeper thoughts through email. Because kind of if it's too long, nobody reads it. And if it's too short, it doesn't contain the content. And I think that was the point where I really, really started thinking about, OK, why do we still have this basic format? Every document is this linear thing when clearly we're getting more and more information. We want to attach more and more data.

And I think this was kind of the problem I was looking at there of I just couldn't really believe that we are in kind of like, I don't know, 30, 40 years of advanced computing and we still don't have anything better. And then I started thinking, and of course I realized that we do have something better. That's how the internet works, right? You know, it's hyperlink, it's hypertext. In fact, it was invented, I think in the seventies, sometimes, you know, a long, time ago. But eventually what happened is it's

Every time somebody tried to create a hypertext editor, it always became too complex. And it ended up also only very technically savvy people understanding or being able to use it. And kind of my idea was of, if we create a hypertext editor for mobile, right, you know, that by definition needs to be simple because you can only have so many buttons you can put there. There's only so many things you can fit on a small screen. And once you figure it out for mobile,

Balint Orosz (02:39.054)
you can scale it up for desktop and it still remains simple. So that was the core idea. And I think that's how the whole thing started of how can we create a system that is easier to manage information and thinking specifically while you're on the go on mobile. And I started working around this in 2018 and at that point this was a pretty big thing because I remember we all had our laptops but we all left our laptops in the office.

So kind of after 5 PM when everybody went home, we were all the time on our mobile. So it was quite different compared to today. But that's where the whole inspiration started from. And then, of course, it grew and it evolved. But I think this kind of frustration of there must be some way better to represent information and to work on it across devices.

Ridd (03:30.542)
It's interesting that theme of starting from mobile and using that as a constraint in the early days to force yourself to arrive at a new simplicity and kind of break the mold of what has become the norm has been a theme. Like that's popped up multiple times. I was just having an episode with the co-founder of Play recently and he shared the exact same thing. It's like, you know, we knew that this was probably going to be on web, but if we started on mobile, we would also guarantee that we'd arrive somewhere different.

Balint Orosz (03:59.683)
Yeah, I think by the time it was 2017, when I really started thinking about it, people already said mobile is figured out, right? Because it was no longer the new avenue. But I still think there's so many things to figure out how it works efficiently. The way I would articulate it is the age of the free exponential growth of you needing to conquer another platform is over.

But I think it's still such an interesting domain to think about. And for me, think this experience came from, Skyscanner, technically my job was to shrink down a desktop website on mobile. Skyscanner is a flight meta search engine. with Flight Search, there's prices, there's outbound times, there's durations. There are just a lot of numbers on a screen. And it makes a lot of sense in a big screen. You can have small table layouts and everything, but in mobile, doesn't.

And we often had this thought experiment thereof, if we really want to do a great app for that product, how would that look? And we always came to the point of the whole user journey would have to change to make sense and how you filter and sort. And I think this was the part where I realized of, it's just often impossible to take a desktop product and have the same product shrink down to a smaller screen. And I didn't want to fall in that trap.

Ridd (05:21.933)
Hmm.

Balint Orosz (05:26.585)
And I think for me personally also, I do have a strong background in mobile. So kind of in most of my career, I've been building, designing, working with mobile apps. So I think it was also my natural habit after I felt I could do something interesting and build a team which could do something interesting. And it's just amazing of how we slid into doing the desktop and web applications as well.

Ridd (05:54.158)
I know when you were first starting, maybe this was a little bit more of a novel idea, but the fact is today, you know, we're recording this in 2025, the year of our Lord. This is a pretty competitive space now. So can you talk a little bit about how you think about differentiating craft in the market today? And then how does that differentiation influence the way that you design the interface?

Balint Orosz (06:18.584)
Yeah, so this was a competitive space, I think, 10 years ago, five years ago, 50 years ago. It's a little bit like, know, weather apps, right? Everybody builds one, and there's tons there. I think for me, the biggest frustration and what really focused was, one really important was is I have a huge respect for the devices you purchase and the devices you buy.

And I think we choose specific devices because assuming there's less of a monetary constraint, which is for some people, but for a lot of people specific in the Apple ecosystem, that's less of a concern. They really want to get the most of it and they really buy it for the design language. And I think around when I started, but even today there was this big trend of just build a web app and package it inside of desktop product with Electron. And while there are...

Nowadays, think some products that do it very, well where you don't notice, on mobile, it gets even worse. So I think one of the really strong differentiator we felt we have is we always want to be as close to the hardware as possible, which should result in the best possible performance. Now, this might be hard to measure because maybe from when you press a letter until then,

appears a screen, it's five milliseconds versus 10 milliseconds, which some people might say you cannot even measure. But when you add up all of those, how fluent a product feels and how it makes you feel when you use it, I think is really important. And when you're thinking about a tool for thinking, for writing, mean, an average user spends two, three hours a day working in craft, it adds up, right? All of the small, unnoticeable frictions add up.

And the other part is, eventually, I think as companies grow, there is this very strong pull of, okay, you now have a lot of user love from individual users. You need to scale. And one very trivial way of scaling in the past couple of years has been going into B2B. And that creates then not just a natural desire to grow the business, but a different set of principles of who you build for.

Balint Orosz (08:40.557)
who is your customer. Eventually you go from having individuals using your product, being your customers, to managers making buying decisions, making those customers. And however you try to balance user experience and all of those, the incentives, the culture, everything adds up to really building a product for the manager and for the business, because they are the ones paying, and they are the ones making the request, and they are the ones you're talking to. And I think what's

What we are trying to do very differently is we want to keep building for the customer. For a long while, and even now, often the biggest question with these businesses is how big can they be, right? Because B2B companies can pay a lot more. And you know, that's probably true. But I think there is a sufficiently large market of individuals who want to use amazing tools, which can make a company like Kraft be successful and sustainable in the long term.

And I think that is a fundamental value for us is we're not, we're not necessarily willing to chase growth because of the money or the profits it can do. And of course we're venture capital funded. So we, we do aim to grow, but we really want to be honest to those principles of just creating a really nice piece of software and, following that

You know, line of, they always say of it's not enough to build a good software, right? You know, you need to market and everything, but there are examples where you build it, it gets better. People keep talking about it and growth eventually accumulates. So in other words, I think a big chunk of our, of our focus, both when we look at what we prioritize in feature development or where we invest in hiring people or what type of talent as a company, it's really around.

building the best product out there possible for the end user and saying no to all of the other things that are very shiny and potentially have a strong business growth potential, but also risk essentially the product diluting and becoming less streamlined and more clunky, if you know what I mean.

Ridd (11:01.889)
Totally. I want to go a little bit deeper there because I think a lot of note-taking apps, maybe even if they could say something similarly, what ends up happening is they design an interface where the goal is just to get out of the way. Like it's like the bare minimum UI possible. And it's pretty clear that's not what you're doing. So can you share a little bit more about what are the North Stars or principles that are guiding the way that you're designing crafts?

Balint Orosz (11:30.463)
So.

In some areas, always tend to refer to, you know, there are interactions in a product which I consider skip pages or skip interactions, like things you don't want to think about, you just want to get over with. And you want to use there, I think, the UI elements, the UX patterns that you don't notice them, you make it unnoticeable. I think one of the really good examples of this is the iPhone's pin or SIM pin entry screen, right?

It's a plain text-filled type of thing. It's so on iOS, but you can see they say this screen is just so you see it once ideally in your lifetime and then you never see it again. So it's not about the light. And then there are other parts of the product where you do want to have a very positive emotion feedback loop. It makes you feel more connected to the product. It makes you feel better. And

And I think that is the hardest thing for us often to figure out is, are we building a core interaction and are we doing something special here which deserves a very strong extra attention? Because too much of these just makes the product feel like, you know, popping everywhere. Like, you know, an animation here, an animation there, it's all not harmonized and it makes it feel too much. But if you don't have this, then it feels way too dry. So I think it's around that balance.

And we, again, it's a little bit for us, we feel that when you're spending two, three hours a day in a tool, it's a little bit your digital home, your digital environment. Like, you know, it's almost like when you look at home offices, which people have where they spend a lot of time and they're a lot more decorated, they look a lot nicer than they used to back in the days when we only spent a couple of hours in it. So I think there is this also is in this nature because craft is, think, a lot more than just note taking. People use it for thinking, sharing documents, creating long form content.

Balint Orosz (13:32.308)
They're spending a lot of time on it and we really want people to feel home inside of it. And I think that is why we're not necessarily looking at everything on the bare minimum, but trying to balance and figure out what matters and what feels good versus what would be just too fancy or too much.

Ridd (13:52.887)
Hmm.

I imagine it's not always obvious where that line exists. Like something like the Doodle Separators comes to mind for me where it's like I've never seen that in any other kind of app. Like it's so...

It's so playful in a way that really distances itself from utility. And it feels fresh. But yeah, I could see how that spectrum of just how personalized and just how many abilities do we give users to make this their own is probably one of the core debates that's happening internally.

Balint Orosz (14:31.666)
It is, it is, think. and we often get it wrong, you know, so we often have things that we do something and users say, is too much, or we're using it for like six months and feel that this isn't working, this is too much. So I think it's a set of experiments and, and a lot of these come from our own, you know, way of doing things like the doodle separators came of one of our internal team members, you know, kept uploading PNGs as images, which had these doodle separators.

because she wanted to use it. And people started liking it more and more and more. And we were like, okay, but could we make this then a core feature? And of course, when we're making it a core feature, when we think about it, okay, it's not just about, we like Doodle, but what if somebody else liked something else? So that's where I think the Customizable Washi tapes, which open up a lot more variety, came into place. But I think this is a very magical thing of being able to

build a product you use every day very extensively is just that connection and that intuition of what could work is such a core part of figuring out how to move forward.

Ridd (15:43.149)
What are some of the challenges that come with designing a product where content is everything and pretty much all of it is user generated so it can almost take any shape?

Balint Orosz (15:55.199)
I'm just gonna fix my camera. It sometimes does this. So I think one of the big challenge for us always has been is what is craft and what is your content? And where is our brand and where is our brand too much? And I think that resulted in us, for instance, we don't have, I think, a sufficiently strong brand, nor visually in other ways. And it's really hard for us to figure it out because

As I said, we want this to fill your space. And you might like our brand colors, or you might not like, but we cannot be too aggressive with this. So I think early on, as I thought about how can we still make crap beautiful? Because it's a lot about texts and documents. And it's not like Netflix or Spotify, cover arts and all sorts of beautiful things. So from early days, we said,

we should put your content everywhere as a design element. So essentially, if you create colorful documents, your craft should become colorful. If you create black and white documents, your craft should become black and white. And we really heavily invested in technology of being able to just render pixel-perfect representation of your documents everywhere you are in the app, using a lot of when you enter a document, the whole window takes over.

like ambient lighting from that document, from the background, current, things like that. So as you move forward, the whole product in some way, you know, reflects the content you're looking at. And I think this is, this is what we're trying to do and emphasize. And this is why we're moving also a lot in, understanding options of how you can easily find styles and customize your documents. And, and through that.

just make the app feel more like you. And it's so super interesting because when we look at some videos of Japanese users, for instance, do, we have this grid format of you can view your documents as a grid on your home screen. And then if you have a cover image, we have a full-size cover image. And their craft looks like a Pinterest board because they always add cover images and they won't have that layout. Well, my craft, I never add cover images. So it looks a lot more like a traditional documents application.

Balint Orosz (18:21.031)
But it's just so fun, I think, to see of how people resonate with that and really customize it to make it feel, again, home for them.

Ridd (18:33.303)
How does that influence the way that the team works? Like even just the way that you approach dummy data. Like whenever I'm designing products that are heavily user generated, it's always kind of a lot of work to make something feel real. How do you approach that problem?

Balint Orosz (18:49.564)
So I have a few weird beliefs about me. I don't really believe that, except for certain circumstances, user testing on non-real product drives reasonable results. And one of the really good examples of that is, again, in my previous job out of this flight minister engine, we tested two variants from the same product or the same feature.

And I wanted to hack the system, so I said, OK, let's have the first variant has $100 flight prices and the second variant has $1,000 flight prices. And essentially, the cheaper or the more expensive variant won. And it became the better one. And I was like, you know what our customers say? The only thing they come to the site is because they want to have the cheapest flight. So it's quite clear we've been testing with people who didn't have a real intent to use it.

And they engage very different because I showed this to a real intent buyer person, they will be like, this is the worst product I have ever seen. So, so I think this grounded these things of we prototype most of the things in the main product and we use it and we have beta programs. So actual users who use craft interface it and use it. We use Figma and design tools a lot, but we think about that as the initial phase of sketching.

and figuring out layouts and laying out concepts. But except for some very small minor features, we never, I think, ever had a thing where the final Figma design, as it were, translated one-to-one to the release features. More often than not, we have significant changes in how certain things behave, because it is really important to just use it in context.

and see the challenges and the benefits of a product in context. And it's interesting also because there are some of the things that we fall in love with the prototype with. We say it doesn't feel like a good idea, but the moment you touch it and interact with it, it just becomes something magical. So I'm very, very big fan of this part of move into the real product as quickly as possible. It might be in the web, in the app.

Balint Orosz (21:08.623)
but see your own data and see the exact workflows you have there.

Ridd (21:13.345)
How does that impact the way that designers and developers collaborate then? Because I could also see the flip side of that being like, well, if Figma is just sketching, then you almost have a little bit more reliance on engineers because the idea is not fully realized until code is behind it.

Balint Orosz (21:30.492)
Yeah, but isn't that how it should work? It should be a collaboration of engineering and design to come up with the best product. So most of the projects start in the traditional design phase where we iterate a lot in Figma. Let's say that is 50 % of the project. And then the other 50 % is designers working really, really closely with engineers and having a very strong feedback loop. And it's challenging, I think,

is specifically when you're hiring. So the people we have kind of really, really enjoy that, and they have a deep respect for each other, design and engineering, and engineering's not pissed off if we need to throw away something. They're not saying, hey, you should have done a better job at designing in the first place, and kind of designers are not upset if they need to change the design for some performance considerations. But it is, it is, I'd say,

Not that natural, specifically in larger organizations. think in smaller companies, you see this more often, but it is just something you have to calculate with. But the really good thing about this is that as the more engineers interact with designers and vice versa, each of them understands the main better. So our engineers know about paddings, the importance of them, animations, curves, how do they work? So you could also look at this as you do train.

people, right, they train each other, which results in having better partners in your work because you can move faster and you can do stuff. So we do have quite a few comments, for instance, from our designers in the code, and we do ask our engineers to create code that designers can read. So all of the variables around paddings and, know, animation curves and colors, you know, well named, separated, so any of them can go in and tweak those. So I think it's a lot of fun once you get used to it.

But at the first, it can be intimidating for some.

Ridd (23:27.425)
How much are designers getting into the code?

Balint Orosz (23:31.042)
It depends on the designer and on the shape of the project. So there are some designers who kind of prefer fix things themselves, and they prefer to tweak parameters and go into the code and build prototypes. And there are designers who do that if that's needed, but they'd rather sit next to somebody or have a call and explain how they think about it and very quickly build and test it that way. So there's no real strong requirement around it.

And kind of obviously then those designers who code less, they are better communicators and you know, they speak better with developers and smile more and engineers and designers who code more, they have less reliance on that. But it's funny because everybody figures out their way. So it's fun to see that as well.

Ridd (24:22.701)
Okay, so I wanna keep going like way deeper into how you work, but maybe first we could just give people a little bit of context. So what's the current state of the team right now? How big is the design team? Anything else that you wanna share in that category just so people understand the lay of the land.

Balint Orosz (24:37.38)
Yes, so total in the product engineering in the company, we have around 25 people who are doing the backend, the web, desktop, and mobile apps. And kind of when we look at the platforms and team, have a three, four person design team, three, four person app team, three, four person web team, I think, four person backend team, and kind of two, three people in QA. And we don't have product.

So I think kind of most teams are the three, four people size. It's a fun size. Everybody knows about everything. And very often, team members can jump into each other. It's also a challenging size because you're enough people to do anything, but it's not enough people to do everything. So it's a tight balance of what you want to get right.

But this is around the size of the organization right now.

Ridd (25:37.262)
Okay, so I wanna pick a project that we can talk about to use as a lens to learn a little bit more about how you work. I'd really like to hear about the quick ad feature on mobile. I keep seeing that on Twitter. It's beautiful. It feels like a breakthrough pattern. How does something like that go from the seed of an idea to hitting production? Like what are the different milestones along the way and how can we use that to just get a better idea of how you all work as a team?

Balint Orosz (26:06.243)
That was a very, very fun project. So essentially, we had this big project called Crafts 3 where it was a very, very big update. We've been working on it for six months, new features. And it included changing the navigation of the iPhone app. So around one, one and a half weeks before the launch, we kept laying this project of, OK, but how will you create something new? Because we knew our

our existing new screen is people don't like it. The way it worked is you press the plus button and then a list came up. Do you want to create a new task, a new reminder, a new document? It was too much cognitive load. So we said, okay, but kind of the solution is quite clear. We just need a context sensitive new button on every screen, right? So if you're on a task screen, creates a task. If you're a document screen, create a document, a calendar, a calendar. And then if you long press it, it brings up the menu.

And we kind of designed it, prototyped it, and kind of our head of design was like, you know, this doesn't feel right. I mean, I get all the logic behind of it and it should feel right, but it's not. And we were like, I think, you know, five days before launch at this point. kind of, you know, we had my co-founder Victor, who's kind of the orchestration of release. And we were telling him, you know, we have a problem. He was like, go figure it out. So when I first started Kraft,

it was about quick capture. And the first part was I said, chat is the dominant interaction on mobile. So let's do text input like it is in chat. So when you press the plus, the keyboard opens up and you type in that small chat button. And when you press send, then that content gets added to the document. And I had a screen recording of this prototype, which I built five, six years ago. I gave it to the designers of

You know, maybe there's something here. And, and I think, you know, three, four hours after there was a first stigma prototype, the next morning we, we did a basic, you know, interactive prototype. said something's there, but it's not perfect. but I think after two days of this very rapid iteration, we landed into understanding of the reason why this works is when you press the press, you know what you want to add into. So you need to get that out on your head.

Balint Orosz (28:27.904)
And you can choose afterwards because you're believed I have it out there. Now I can decide where I want to put it. But I also think this is a, it's, it's both a very common way of how we do things in a very uncommon way. So, so technically I believe that ideas are super fragile, right? You have this, you know, random idea and either you act on it almost in the moment and try to make it work, or it's going to fade away. It's not like ideas can be put on the shelf.

And, and we have a huge amount of these, let's act on this, which totally don't work out and go in the bin. But some of our best, you know, features, some of our best, you know, concepts come out of these, you know, very fragile and very rapid interactions. So much so that, you know, from user feedback, from what we're seeing, quick add, it's clear that it's becoming a lot more important in the product. And we have a.

a lot of things planning which we can build on top of that. So it's fundamentally interesting how a fleeting feeling of this solution is not good enough. Let's try something radically new. You know, have that idea do it can lead to then essentially we're going to have a three, four months, you know, more structured project around how to get a lot more of the quick ad and this type of let just people get from their head into craft a lot faster.

So that's fascinating in some ways.

Ridd (29:58.7)
I love that because you're not just solving the problem in an interesting way in the eleventh hour, but you're also identifying a building block that you can use throughout the rest of the system.

Balint Orosz (30:08.855)
Yeah, those are the best ones again like out of 10 20 50 of these ideas one ends up being this You know successful, but you do have to do all of them because you never know what front right?

Ridd (30:23.469)
So I'm a big believer in this, you know, acting on inspiration in the moment. And a lot of times when we're solving these problems, that's what sparks the ideas that, you know, send us down this rabbit trail. And yeah, maybe some of them do work out really well. Kind of the flip side of that is a little bit more of the strategic planning and road mapping. Can you give us a sense about how you approach that at craft?

Balint Orosz (30:46.847)
Yeah, so we have a very solid understanding of the two, three biggest problems we want to tackle in a given year. And that is based on user inputs, our belief where the market is going, talking to customers, data. So we have all the traditional stack, which formulate of we need to be here in one year if we want to.

want to execute our vision. But it's always interesting of when you go from, in a city, from point to point, You know the endpoint, but there are at least, even Google Maps gives you 10 different variations of how you can get there. And for us, it's, well, it's never really clear the order we're going to get there. So I like to joke, and there's always some truth in these jokes, that in Craft we have two roadmaps. We have the next two weeks, and we have the next one year.

But it is in some ways true, in a lot of ways, because we really want to be able to act on the things we learn and act on the insights we get while delivering things. And we also want to have space for experimentation. So if we would need to have a three-month roadmap, the question is, OK, but how do you fund non-critical projects, which might become something super, super important?

You know, having this every two weeks, can re-evaluate if you want to fund an idea more, fund the project more. There's no pressure that you, like we as a leadership, let's say, to commit to, you know, one project that seems powerful for three months. Every two weeks, we can have a check-in and see if we still believe in it, if the progress is, you know, towards what feels good.

So, so I think that is a not a real answer for that, but this is kind of what happens. And a lot of people again, initially are super frustrated about this because, okay, but how do I plan my holidays? When is the big release going to be and things like that. And it's like, just, we're just saying like, we try to operate in a way where nobody is required for a release. So just take your holidays, whatever you feel you have to take your holidays because we won't be able to schedule right now for six months in advance.

Ridd (33:10.945)
Hmm.

the operating on two weeks in a year, like I can see lot of benefit of that. And there's like the flexibility room for experimentation. Can you talk a little bit about how designers can either fill in the gaps or even like what it looks like to effectively make a case for why something has or is is worthy of that level of investment?

Balint Orosz (33:38.207)
Yeah, I think also a roadmap has around 50 % of it is what I would call reactive. So we do something, we realize something is missing, like we release right now tasks and people really want to have recurring tasks. So that is a project that is reactive. It's more kind of a formal. Let's say we fund that and we do that. And then there's this other part where let's say things about what we want to do with AI.

It's clear we don't want to do just AI for the sake of AI, but we're starting to get a really good feeling of what could work. And for instance, how we could create an interface that merges voice with keyboard, with mouse, with touch, and you can switch anytime. It's kind of a conceptual phase. And kind of, you know, the designers who really want to do things like that, we a little bit expect them to take initiative, have come forward with idea and almost say, can I spend a week on this to figure out more?

And then we say, spend a week on it. And after a week, they're like, what did you learn? And do we want to do another week of work? But Next3AI, a really good example of this is we're now experimenting with shaders. So when you look at animation and design, it's quite clear that we're reaching peak moving rectangles beautifully on the screen. And Apple is doing a really good job at showcasing how

shaders on the screen can create really nice effects like with the new Apple intelligence, but also their airdrop effects. It has a new sense of magic. And we feel for certain wow moments, we could use that very well as well. But we're never going to fund a three-month project for that. So what we kind of want is somebody to come forward of they feel for some reasons. And I think for us to break through is that LLMs can now generate shader code.

And because it's very hard for designers to understand shader code, even for engineers, it's hard. But with that insight, we're saying we actually have a shot at prototyping shaders and getting a feel of how they work. So they come forward and usually it doesn't happen of, you can do that from tomorrow. But in the next two weeks cycle, we can already plan in a way that there's a couple of days, a full week or something like that where you can go and instrument with that. So in this sense, we do expect designers to be a lot more

Balint Orosz (35:59.952)
ownership oriented of figuring out what they feel is right. This also means thinking more about the product as well and understanding customers. And I think this is also this designer-engineer collaboration and designers taking lead is why we don't have a traditional product management layer because designers pretty much together with looking at engineers collaborate with customer support, understand user feedback and kind of see the whole picture.

which makes them able to detect and suggest these opportunities. And then, for instance, I also have sometimes a few where I just drop those in, maybe somebody picks it up. So I think this is more of a 50-50 type of ballpark rule of reactive versus trying to be more experimental.

Ridd (36:47.48)
Yeah, I mean honestly, it sounds like a blast to work in that environment because you do have to wear the product strategy hat a little bit. Like you have to think about, okay, what do we need here and what can I push forward to make that happen?

Balint Orosz (36:55.892)
You know it.

Balint Orosz (37:01.149)
Yeah, it's, you know, these things are always because everybody wants ownership, but fundamentally a lot of people get scared when they see the responsibility that comes with ownership and decisions you need to make. So I think if you're the person who's really okay with it, it's very hard to take ownership on something. For people who don't do well, it's a lot of stress, they can get burned out. But if you, I always tell people of,

we are creating digital note-taking software. We essentially are really careful about data security, syncing stability. We don't iterate there. Everything is heavily tested, so there's never ever any data loss. If we create the wrong type of animation, we're in that concept of we'll just remove it. So we want to be very playful here.

And it's interesting because some customers like that and some users just hate it. say like, you know, hey guys, you're changing something every six months or every three months. And I just cannot take it anymore. And in some ways they're right, right? Because when you change something, you need to relearn something, but we still feel where there's so much we need to figure out to arrive to a point where, where we're happy to, you know, spend a lot more time saying this is good enough that it's just something we need to be very conscious of, of doing.

So yeah, I think it's a trade off. You get a lot of ownership, but we expect a lot of responsibility in exchange.

Ridd (38:35.533)
Can we talk about the scale of change that's happening? Because you've been working on this for like six years and even I have been able to notice a pretty significant interface overhauls. So is there an example you could talk through about like, hey, this is why we arrived at a somewhat larger change and how we approached it?

Balint Orosz (38:55.281)
Yeah, so most of those are typically when the existing architectures start to break. So for instance, the very, very first version of craft was just a stream. And you had at the bottom a segmented control. One was recent and one was archived. And we set kind of your...

your documents, your note taking should be like email, right? You have search and then you have one stream of things because then it's very simple to navigate. But then people came and they said they want to have folders. And we're like thinking of, you know, that's reasonable. People are used to folders. Apple tried to avoid having files and folders on the iPhone. They resisted it, I think, for 10 years, but even they said they cannot do it. And then you realize, okay, you need to redesign the navigation, right?

you know, folders don't fit well in the segmented control. And I think this is what we face is, since we own, even when we talk about our vision, we really have a one year of more concrete understanding where we're gonna be. I think I can paint a very good picture where we're gonna be in one year, but I don't know where we're gonna be in five years. And the thing that happens in a lot of companies is they end up as they expand and shift focus areas is you open a screen and you have 36 buttons.

So, like, you know, all of them are beautiful because they have a design system, but it's 36 buttons and eventually that complexity adds up. But because when you have a more mature years of base changes so hard, so you always reach a phase when, you know, not changing ain't that bad because if you're making money, you're risking losing money. and there's a phase in life when, Amazon had this, it's always day one where you just say aggressively, we want to change. And for us, whenever we.

we introduce features or new concept like, know, even right now we already have five tabs in the iPhone app, right? So you cannot have six, that's too much. But if we really double down on quick capture, you know, that probably needs to have its own tab as well. So then what do you do? You need to simplify something so you can expand in other areas. So I think most of our redesigned are really about us looking of with every phase we wanna have, you know,

Ridd (40:58.19)
Mm-hmm.

Balint Orosz (41:18.82)
a somewhat scalable system, but we never really think about how it's going to scale for five years. We try to focus on how for the foreseeable future this structure and this, you know, design hand was what we want, knowing that we might in one or two years need to override it. And we're okay with that.

Ridd (41:38.007)
How would you describe the fidelity level of that one year plan? Like what are you equipping designers with or how much detail are you giving them to work backwards from to identify the right opportunities?

Balint Orosz (41:51.663)
I think we're working a lot together, right? So I've been doing, you know, I've been essentially head of design for mostly up until kind of last year. So I think that's also one of the reasons why designers are so close to business and product and, you know, decision making. So I'd say I kind of share everything with them. Like,

Sometimes I even share my board meeting notes. know, sometimes those contain, you know, sensitive information, but I don't, but sometimes I do. I'm a big believer in this. People need to be able to consume information. They don't need to react on everything, but they do need to be able to consume because the challenge is if you're talking through problems with somebody, you really want to have them on.

the same level you are, right? Because otherwise you're gonna dominate, you're gonna bring in a piece of information they had no access to, so it's not going to be a fair debate. And I really want people to challenge me, and I really want them to come up with new ideas and figure out complex problems. And the only way you do that is if you share a lot. This means I often share thoughts that in like two weeks we say it was a terrible idea, we're not gonna do that anyhow, because it was premature. But again, I'd rather take the risk of

them getting premature information and understanding that, my God, I don't have everything figured out in every month, you know, there are changes to our plans, then limit the access to information. So that's how I think about that.

Ridd (43:28.715)
Yeah. I want to talk about another project really quickly, which you have mentioned briefly, which is the tasks in craft three. Cause you've basically made those a first class citizen now. And I'm always interested in hearing how teams design features that have like a ton of precedent online. Like in many ways, tasks are a solved problem. There's so many examples to pull from. So how did you figure out what the design of

would be inside of craft and what your take should be.

Balint Orosz (44:00.09)
So I was so shocked of the complexity of that project because as you say, it's a fricking task, it's a checkbox. What can be so complex about it, right? And these problems end up being the most complex problems because the whole task project came in the way where people have been telling us they need databases in the product because they want to store more structured information. And we're like, why do you want it? And they're just, I need it, I need it, OK? We're like, OK, you need it.

So we said, why don't we build more structure in the product? Because that's what we felt is not databases thereafter, but they want to have information easier to access, recall in a more structured way rather than just free from search. So we built this thing called Objects, which was a little bit of an object-oriented note-taking system. So every document you create could have attributes, and you could create

these very interesting systems inside of space. And we release this in a beta for like 2,000 users. And we've been talking to those users and things like that. And we're realizing 90 % of them were creating two type of object types there, projects and tasks. And the third one was people, right? So the CRP's case. So we're like, aha, OK. So now we understand why people want more structure, because where do you need structure most? Like project management, right? You want to make sure you have an overview. You want to see that.

So we were thinking of, that's great, but there's probably, when so many people want this functionality, we need to make it a core part of craft. Because we already have something called check boxes, which relate to that. So then we started looking at how do we solve this? Because fundamentally, there's two ways you can solve this. If you solve it for the individual user, you have a check box. But if you want this to work collaboratively, you have this table type of thing, where you have a status.

drop downs and it's no longer a checkbox. And then we said, yeah, kind of we want to have the checkbox because we already have the checkbox and we don't want to have another type of thing. And I think through this thinking, we also realized that the reason people want so much overview of task and craft, because when they write their notes, their documents, tasks come in there in context. So kind of.

Balint Orosz (46:25.092)
They already have the surrounding context there, which other task manager apps don't have it. And that's why it's more valuable for them. So that's when they said, okay, everything should be built around the documents. So that's when the task page, have, you know, everything organized from your documents. But there was this thing of the quick capture, right? Of with tasks, you have this thing. I just want to quickly add it to my inbox, which is really much around the GTD mythology. And that's where we ended up with that inbox, but it was a super

long process from identifying there's something there to actually figuring out both what people want and what is, think, the way I'd say what feels natural inside of our product. Because there are so many ways to do this well. And I think there are so many different implementations of this. And what was for us very important that it works seamlessly. So you don't have to change your workflow or as we introduced it, it won't upset your workflow. You can still keep using Craft for Notes.

And I think that was the, and almost like it was four months to figure this out and then we built it in two months. So it's shocking of, of, of nowadays, how much longer it takes to figure stuff out versus executing when you know.

Ridd (47:36.833)
Yeah, I love it as an example too of being able to understand the underlying why behind something that users are asking for. Because there's a world where you would have just taken that initial feedback at face value and built this robust connected database system.

Balint Orosz (47:54.424)
Yeah, which we did and kind of again, it was a very interesting thing because what happened is I went on holidays after the beta release because we did that in August and you know, I came back and again, our, you know, head of design was like, you know, I read through thousands of feedback, talked with customers and kind of they don't want this object. This is not what they want. So essentially what they said is, you know, let's roll back four months of work. And I think you really need people who

are okay to say that to you of, what we're doing is not working, but the silver lining is we kind of now know better what we need to do. And again, when I went to the board meeting of saying, yeah, we had this concept, it's not working, it's kind of sometimes hard, but in retrospect, it's very good to be able to do those.

Ridd (48:42.638)
Because one of the ideas that I'm thinking a lot about right now is how being wrong is just one of the fastest ways to actually push things along and make progress. so like, so often I reflect even on my own journey where I've spent so much time trying to be right, where if I would have rather just put something out there that was wrong, we could get to the end point so much more quickly.

Balint Orosz (49:06.145)
Yeah, I think it's always a challenge of how do you understand if you're right or wrong. And I think this is a question we keep facing again and again, because here we could understand it quite well. And I think for us, this is why the beta testing community who are actual craft users and testing new features is so valuable, because just from data or just from user interviews alone,

I don't think we would have had sufficient evidence to make that call.

Ridd (49:40.173)
Yeah. Can you touch on briefly just the role that components and systems play in this world where you are pretty quick to reinvent the product each year?

Balint Orosz (49:53.709)
Yes. I think one thing we realized is because we like to tweak things, if we build components, they will get messy very quickly. And what ends up happening is you're essentially slower to build with components than starting from scratch, right? Because if you have a button that has 25 properties, when you add the 26th, it's just going to fall apart. So I think we...

We want to give a tool chain to designers and developers to be able to build very quickly, very high quality experiences. And for some companies that manifest in atomic design system and components, but in our cases, I think it's a little bit different. So we do have some, you know, very standard things, I almost call them. Like we have an animation engine.

that is super powerful, the curves are super monitored, and how animations are wrapped inside of each other and how they inherit is very well defined. Which means if you ever want to do an animation where the entire screen moves, even if it's 25 components, all of them will be synchronized independent of what's happening in those components. We also realized that we're dealing with text, and often we need to show a lot of text next to each other, let's say a breadcrumb.

And for instance, showing an ellipsis in a breadcrumb on a mobile takes like three, four characters. But for instance, having a gradient fader on top of it, you see two characters more. So we created this component that on any label with one line, you can apply this faded clipping. So whenever you're with that problem, you can access it. But also, we noticed that

One of the things we use a lot is we use this more gradient, colorful material so that whatever you have, as I said, in your document, you can take over the colors of that. So we build this material that again, with one line, you can make any view, you know, participate in that glowing system. So we don't have a button component or we don't have a dropdown component, but what we can do is we can build a

Balint Orosz (52:15.676)
a segmented control that is just as beautiful or more beautiful than any out there in like one or two hours. And we're saying that is a lot more important for us to do because essentially because of this, have a little bit of too many corner radius differences in the product and you know, it's not everything's on grid. At the same time, we can do those very quick prototyping loops.

with new ideas, which we've talked about at the start. And I think that is, has always been for me very important is how fast can people create greenfield projects. You should still capture the feeling and overall essence of the environment you operate in, in this perspective craft. So you shouldn't, you know, bring a totally different visual style, but, but if you can create something new from in one hour, then kind of, doesn't really matter if you reuse it or not, because you're not spending that much time there.

And, and again, this is not, not trivial, I think. And, and I've been, I think I first started working with components like 20 years ago, something that when Flash and Flex, they already had this, you know, components part and I always struggled with it. And, and I was also super shocked though, where Apple doesn't really have, it has very, very few components compared to, to other mature, you know, design languages out there. So I like to be able to treat.

the screen as a canvas and paint it because that gives you an ultimate control and creativity. It adds to complexity, but that might be the cost of innovation.

Ridd (53:56.908)
Hmm, I love that.

I want to make sure we're not missing anything here because you've won Mac App of the Year, Apple Design Finalist. You're obviously doing something right. You've talked a little bit about the engineering collaboration. We've also talked about the speed of the app itself and how much of an emphasis that is. What else are you doing to achieve this level of design excellence consistently?

Balint Orosz (54:26.987)
So I think it also relates to the navigation and the redesign discussions of, I don't think we ever think we're good enough. So that doesn't mean we're not proud of our work or we're not happy where we are. But every day, every release, we want to get better. And we want to do it well. And we're super pragmatic about it. So I think we're doing a lot of unorthodox stuff, like,

we still use manual layout. think AutoLayout was introduced in 2014, 2013, since there's SwiftUI and all of those things. But we all look those of being abstractions, which the CPU technically can take it now because we have faster CPUs than 10 years ago, but it still takes cycles away from it, And kind of the less free space, for instance, you have...

In your layout code, that means let's say the data sync is going to be slower or the updates aren't going to be added that file. So when we look at a new technology, we're always like, does it solve a problem we have? And if it doesn't, we just don't adopt it if we don't need to adopt it. So I think in that way, we're very conservative. At the other side, just because we have a solution that seems to be okay for one problem, we do try to create a better version of it.

And I think this is a very interesting thing because I think we're the only product of our complexity which uses the same code base across iPhone, iPad, and Mac, right? Most of the times people have a responsive web app, but then the native iPhone app is a completely different one. And this man, had, even Apple didn't have, I don't think they have figured out up until today how does Apple's design, the iOS design system, and the Mac design system, where do they meet?

Right? They're there, there's in such different directions. But because we had one code base and we had this principle of the iPhone app should do the exact same things as the Mac app. should be no differences. Right? We, we, we had to iterate so much on figuring out what are the things that make this possible that we could just never really say of we figured that now out. So I think that is a big chunk of why.

Balint Orosz (56:50.473)
we keep getting better and I think that is appreciated by a lot of the people who are following us of consistently trying to tackle these problems again and again and again.

Ridd (57:02.349)
Before I let you go, now that we have an understanding of just how you all think and how you work, I'd like to understand a little bit about what you believe about the types of designers that thrive in this environment. So can you just talk a bit about the core skills or traits that you prioritize when thinking about the types of designers that you want to work alongside?

Balint Orosz (57:30.045)
Yeah, it's interesting because we don't have one specific type. So all of our designers are super, super different. And we're really looking to, they complement each other. But really, I think the most important thing for me is what I call strong values to see how. So you need to really believe in things, but you really need to be open to re-evaluate those things and learn new things.

That is, I think, one thing. And the other is, which I found super powerful in designers, is what I call systems thinking. So there are designers who make so beautiful animations and make the screen look like you want to lick it. But if you don't understand how things connect effortlessly and things get

quite complicated quite soon, even, you know, don't know, take a guess, right? There's some serious depth inside of there. And once you start to untangle the problem, you get this, this maze. And since we require designers to think about product, you know, think about the impact of this, you know, talk with engineering, they are in the deep of this. So the designers, think who are most successful in craft really have this, this strong desire, the systems thinking.

And also they continuously develop this through readings, through looking at new things, being very curious. But again, I'm shocked of we do have designers who are really strong in visual design and we do have designers who don't actually prefer visual design at all. We have designers who love coding and we have designers who don't. They go into code, like if that helps them get their goal, but you know, if they had a choice, they wouldn't. So I think it's a lot about these more of these personal

characteristics and interests rather than their existing scales apart from again the system design.

Ridd (59:28.129)
I know this is a hard follow up question, but I want to try to go a little bit deeper into the systems thinking piece and make that more practical because it's been a theme on the show where multiple design leaders have come on and said, yeah, we want to prioritize systems thinking. And I know that there's at least one person listening that's like, okay, great. What the heck does that even mean? Like, how do I grow that muscle? So I'm wondering if you could speak to that person before I let you go.

Balint Orosz (59:51.4)
So one of the really interesting examples is, for us, keyboard shortcuts. So you think it's a really simple thing, because I press a keyboard shortcut and something should happen. But the thing is, how do you ensure that on every screen you have, you have the right keyboard shortcuts? How do you categorize keyboard shortcuts? Maybe there's a category of there's window-related keyboard shortcuts, there's selection-related, and then there's screen-related.

Or maybe there are keyboard shortcuts that are always available, like the Escape and Return key, and there are keyboard shortcuts which are optionally available. Now, then in the Mac, based on the keyboard shortcuts, you need to be able to map them to context menus, the right-click menus, essentially. And now, we're in our phase where we also have the slash menu. Most apps now have a command bar where you want to have the same action as you have in keyboard shortcuts. And potentially, you also want to be able to activate them with voice.

So you have this problem set and you need to able to somehow find a grouping that is very logical and can be executed very, very well. So I think this is an example where something as for us users, it just feels so simple, but getting and understanding all of the complexity and creating a mapping of how this should work requires a very analytical thinking of understanding

how the app works, how the user thinks, what are the system requirements, and how can you create one system that satisfies them all. That is, I think, one of the most recent examples. And we're struggling with that as well. So it's not an easy thing, but we're getting there.

Ridd (01:01:32.852)
Yeah, no I think that's a great example. It's something that there's just so many conflicting goals and like one thing makes sense over here and you're like 90 % away from figuring out the puzzle and then like you identify a little building block or some requirement that just like breaks everything and you kind of have to take a big step back. Like I think that's a really, it's an apt example for sure.

Ridd (01:01:58.737)
Um, before I let you go, mean, is anything, anything that you feel like we haven't covered that you'd like to talk about? Otherwise, this has been really great.

Balint Orosz (01:02:11.13)
No, I think kind of we touched those things we also had in the interim conversation. I'll also just quick take a quick note.

Balint Orosz (01:02:24.642)
No, I think we did touch everything.

Ridd (01:02:27.025)
I think so too. I'm really pleased with it. So let's wrap it up here. Well, this has been amazing. You all have built something really special and it's very evident the moment that you start using the product. thank you for coming on and pulling back the curtain and talking a little bit about how you work and how you think. And it's been really fun.

Balint Orosz (01:02:45.872)
Thank you for having me. I enjoyed the conversation.

