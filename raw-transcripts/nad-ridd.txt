Ridd (00:00.361)
How do you pronounce your name exactly? So I nail it in that intro.

Nad (00:05.75)
and add Chishti.

Ridd (00:07.593)
Shishti, okay. That's what I thought. I just have an Indian wife and Indian in-laws, and if I get it wrong, then they let me know. Because my father-in-law listens to every episode, and so he'll just be like, you know, don't think you did the pronunciation very well on that one. So, glad I got that out of the way. Okay, okay, cool, cool. All right, so tell me the story of how'd you get to lovable?

Nad (00:13.432)
Until next time.

Nad (00:23.886)
Amazing. Well, you nailed it on that on practice round. So you're doing good.

Nad (00:32.694)
Yeah, so I was basically hacking around with LLMs in my spare time as like more of a hobby, you know, kind of got infected with the curiosity, I guess the same as the rest of the world did with chat GBT. But I was super curious about like what I could use them for in design. And kind of at the time I was working at a scale up that was working on kind of secure messaging. And we had really, really good traction in public sector and we had to do all this kind of

design work around things like accessibility and contrast ratios and meeting different accessibility standards for different platforms and different environments. And it was all quite rewarding but a little bit grueling, I think, for the team. And so I started to build these little utilities using LLMs where I could do things like give an accent color to them and then use computer vision models to then create a tailwind color scale from a brand color or something like that and then do a cross-check of

you know, what are the contrast ratios when these different color combos are working and stuff like that. And kind of built, started building these little design utilities. And then I just got completely bitten by this bug of like, wow, this just actually feels like this is what the future is going to be like, rather than us having to kind of manually do everything ourselves. And so I started experimenting with that. And then that led me to an open source project called GPT engineer, which was a project made by Anton, who's one of our founders.

where he had basically started experiments and got LLMs for kind of the same reason, but in completely in parallel over in Sweden, where he felt that he was a CTO of a YC startup, really loved what he was doing, but he actually got quite frustrated because he thought that all of his engineering peers were being too unimaginative with LLMs. So he would be able to see like, I don't know, five, 10 years into the future and he'd be thinking...

you know, most code in the world is going to be written by RLMs and people would say no to him and sort of tell him he was wrong. So he got really frustrated and he put together a proof of concept called GPT engineer, which was basically a command line tool where you ask the AI to build something. If it doesn't know what you mean, it asks you a question back and otherwise it just builds, you know, builds for you. He built that and then overnight, well, not quite overnight, that became one of the largest, most popular code gen.

Nad (02:56.75)
projects on GitHub. And so that went from zero to like 52,000 stars on GitHub. And so, yeah, I basically found that project, started playing around with it, then reached out to Anton and did some advisory stuff to begin with. like a bit of contracting and a little bit of like, okay, let's go from like zero design to some design. But then flew over to meet the team in person. And then sort of since then basically just decided to go all in.

Ridd (03:27.743)
Quick context, how much of a technical background do you have as a designer?

Nad (03:32.767)
I, I would never call myself an engineer, but I've always seen it as a, almost a professional responsibility to sort of really understand like my materials. And so I've just always hacked to get a front end and I've always kind of strived to be technical enough that I can have a high frequency, high bandwidth conversation with the people I'm working really closely with. so.

Yeah, so I could understand say like I could go quite deep actually on things like technical architecture But always in a way that kind of relates back to design and so I would say engineering minded in the abstract and sort of I Yeah, and I can communicate very well in engineers

Ridd (04:16.413)
It's cool because you're the perfect type of person that then gets superpowers from a product like lovable and you get to create that future. So I would imagine it's quite fulfilling right now.

Nad (04:25.89)
Yeah, 100%. And it's like, I feel very fortunate with sort of my, my kind of shape and skill set and sort of where, where kind of all of this is going. But I also think it's a bit of a correction in some sense as well. Like I think, I dunno, like as designers, we know that like form follows function and that like they're as important as each other. But I feel like in the digital design world, we just kind of obsess over form. And so I think like now, at least with AI, we can sort of widen back again and kind of,

know, both sides and also be way more cross-domain and way more cross-functional.

Ridd (05:02.175)
Okay, so let's talk about Loveable now. So roughly like 10 engineers, every day there's a new AI advancement. It's the fastest growing startup in European history. What the heck is that like as the sole designer?

Nad (05:16.878)
Really fun, I guess, first of all. There's definitely stressful moments or moments of being underwater, but overall energy giving rather than energy taking. I think that's the most important thing because if that wasn't the case, then everything else would more difficult. But super high-paced. Internally and culturally, we put a very, very high emphasis on maximizing learning above everything else.

And so the way that we think about things and the way that I kind of work is I'm trying to challenge myself across both individual velocity, but also team velocity. And so for me, what that means is as a designer, I'm an enabler. And so the way that I see things is that design decisions are happening all of the time. Like everyone in every single team, everywhere is making decisions that in some way will resolve into user impact at the end of the day. And so.

Like my job is to enable kind of higher quality decisions across the board, rather than making all those decisions myself and then waterfalling them onto the team. And so what that means in practice is for us, lot of the engineers are carrying things end to end, like as much as possible. And I'm basically kind of guiding them. And so it's less so much about like, okay, here's the perfect design that will exist in the...

in the abstract on a figler canvas and then we go and create it and more so about, okay, let's align first of all on what problems we're going to solve. The engineers have a lot of attitude, latitude on how to solve those. And then we kind of pair up on the best user experience along the way.

Ridd (07:01.823)
When it makes sense, you're basically removing yourself as a bottleneck when you're operating at a level of velocity that is required in this type of industry in this stage of the company.

Nad (07:11.692)
Yeah, exactly. I think that even when I've been in larger teams, I've found this to be a healthy mode of operation as well. Because first of all, it's not that designers have the best ideas, unfortunately. The very, very best things happen from collaborating and also come from the most unexpected places. And so I've always tried really hard to avoid...

avoid this sort of feeling of waterfall or that things are either designed or they're not designed. When the reality is that if people can update the products, like it's always getting designed by someone.

Ridd (07:50.602)
Yeah. I'm sure there's somebody listening right now that's like, well, how do you ensure the right level of quality in the product when engineering in theory could take smaller things end to end and everything's kind of being shaped all at once. And especially as the first designer, I don't know if you've ever experienced this. I've sometimes felt this like fear of pushing something to prod that.

isn't up to my bar because I know like it's never going to get prioritized like everything's moving too quickly where that thing might be cemented for a full year as the product roadmap grows.

Nad (08:26.798)
Yeah, 100%. So I, the way that I think about this is, I think about this as almost like a deficit. And so I think about quality as debt. And so I'm never thinking about like quality being this bar that needs to be met. It's more so this, this almost this deficit or this feeling that can go up and down. And so for sure, there's features that go out where like we're in debt. And so we need to pay off that debt in future.

But yeah, but I see this sort of like living thing where we create debt and we pay it off. And it's just this constant, this constant moving cycle. Yeah, and the reason why I thinking about, think about quality as debt rather than a bar is that it also means that we can translate those conversations internally to things like technical debt. And it becomes very, very easy to then advocate for, you know, paying off some of this design debt alongside technical debt.

Ridd (09:21.075)
Hmm. You've done the founding designer role multiple times now. So before we get into the weeds of how you work at lovable, I kind of want to stay a little bit higher level and tap into your perspective as someone who has been in this situation multiple times. And at least for me, every time I start with kind of the blank canvas as the first designer, it's like this opportunity to.

take everything that I've learned, all my past experiences, and figure out the right things that I wanna tweak or the ways that I wanna do differently. And I'm curious if that resonates and if there are certain ways that you're taking advantage of this blank slate as a designer at Loveable.

Nad (10:00.75)
Yeah, for sure. I the way that I think about it is that I really love working with founders. so like founders are great because I think it takes a lot of conviction to sort of go from something just never existing or not existing at all. So like, okay, this is actually going to exist out in the world. And as a first designer, I think you sit in this intersection of founders and the market.

And so the kind of what you're doing is just sort of trying to tap into this raw ambition, raw conviction, and kind of make it understandable for everyone else. And there should be this sort of healthy push-pull of, know, there's things that just exist because that's, you know, that was in the original vision of the team or individual people or whatever. And there's other things where you get completely led by the market and it's more so about, we were completely wrong about this. But here's these, these other amazing things that, you know, surprise you and take you by surprise.

And so, yeah, I feel like I maybe didn't answer your question, but I think what I find repeatedly interesting is sitting between these two and having a healthy push-pull between them.

Ridd (11:11.837)
Any advice for someone who's interested in designing at startups that they could kind of pull from or tap into some of your learnings for how to succeed in that environment where you're sitting in between the market and the founder and everything's moving so quickly?

Nad (11:28.706)
Yeah, I think be insanely curious, learn extremely quickly, don't fall in love with your ideas because they're going to be wrong and just iterate. like the everything that, you know, every single startup trope you've heard of like talk to your users, talk to your customers, you know, build what people want. Just do that like on repeat and like everything else will kind of fall out of it. But for sure.

I think the biggest enabler for me has been constant learning. so, you know, learning both about users, the market, like how your product's doing, where it's failing, but also learning about people as well. like, I'd really recommend like getting to know the people you've worked the closest with as well as you can, you know, figure out. think designers actually have such a superpower and will anyone that has any kind of research discipline, like the fact that we get taught and we learn how to, you know,

talk to people, decode them into goals, desires, fears. Like just apply those research superpowers to absolutely everything. Like apply it to, I don't know, even talking to a finance person about like how their finance operations are going or their reporting processes, like whatever, but just go around the entire team or the entire org and just pretend it's a user research problem. And yeah, if you do that on repeat, I think there's actually almost nothing that can't be solved.

Ridd (12:57.885)
love that because it's even great advice for how to interface with a founder too. Like treating them like a research project, helping them navigate the weeds of their own mind and all of the ideas and untangling things. think that's like something that I've kind of picked up from a lot of these conversations is that a trait of a great first designer is being an effective thought partner for that founder and helping them even sequence and think through.

all of the ideas, know, because there's a million ideas, all of them are good. Okay, well, how do we make sense of the right ones in the right order and what good ideas to ignore in the early stages?

Nad (13:34.479)
Yeah, 100%. I think you have to, I think it comes with time, but I think once you have a good amount of trust and a good amount of gel, you start to build a bit of intuition around like, okay, what are the really noisy ideas where these are probably just never gonna work versus what are the ones that we should entertain a little bit because there's probably a sliver of one aspect or one shade of it that could have a completely outsized impact if this works. But yeah, I completely agree.

Ridd (14:05.887)
Can we double click on that piece? Because you're in an interesting place now where, yeah, that's like a universal part of being a startup designer, but you're also designing in a space where you're kind of just betting on a massive amount of technological breakthrough, which will change the entire industry. And so my sense is you're probably kind of straddling this.

these two worlds of what's possible today versus where this all might go. And how does that impact the way that you explore and test out different ideas, even with, even in conversation with a founder.

Nad (14:40.172)
Yeah, so I think again, like it all comes down to learning. like we, what I think about and what we think about as a team a lot is just how, how do we maximize our learning in the shortest scale possible? And so what that means is like lots of rapid, scrappy experimentation, lots of, you know, being willing to be wronged and just putting things out there to kind of see what sticks. And so where we have

failed actually has been when we've tried to be too visionary. And so there's been a couple of projects or a couple of angles where we've worked on a problem and we've thought like, okay, the models are going to do this in like six months time. And actually in some cases, you've listened too much to the foundation model providers where they've kind of said like, these things are on the horizon. So therefore you should be thinking about building in this way for like nine months time or whatever. Whenever we've gone down that route, we've had suboptimal results. Whereas whenever we've

really reduced our iteration cycles, really spoken deeply to our users, really shipped small, small pieces first, and then kind of built iteratively from there. We've generally kind of come to a good outcome. And so, yeah, I think that was true pre-AI, that you should always be scoping things down to the smallest version possible. I think it's still true. I think there's obviously going to be still big bets, especially when there's...

the huge step change in like model capability. Like you need to be ready for that. But again, like even learning with a new model, think you should approach that very iteratively of starting small and then building up slowly from there.

Ridd (16:21.183)
wanna go really deep into how you work and maybe we could use the visual edits feature that you just released as kind of a window into just what day to day is and how you work through different ideas. And so maybe we could start all the way at the very beginning when presumably you've identified this broad opportunity space. How were you then as a designer exploring and bringing clarity to what that could be?

Nad (16:49.388)
Yeah. So I think actually if I challenge myself to really, really go back. So we had this kind of deep fundamental philosophical belief that the best AI engineer or the best product of our kind of shape would almost feel like a whizzy big tool. It would be like instant feedback the same way that if you, I don't know, draw a rectangle on a canvas in Figma, it's just there instantly at, I don't know.

120 frames per second, you, or whatever your screen is refreshing at. And we wanted that to feel, we wanted our product to feel like as instant as that. Like since day one, we just sort of felt that that's going to enable, you know, it's going to promote the best, it's going to promote being able to build the best products. And some of our competitors didn't think like this at all. So like obviously super famously, like Cognition launched Devin and they just went.

full blown agent of like, actually LLMs can write code. Instead, we're going to visualize like a desktop and sort of you're going to fire something over to this engineer and it's going to spend four hours processing things and then come back or whatever. And so there's obviously two extremes between a WYSIWYG tool and that, but we were always trying to figure out like, where do we sit along this scale? And every single time we index more on, you know, back on like instant feedback, we never regretted it. And so since day one, we always wanted to have

We always wanted the core experience to be as rewarding as possible, as fast as possible. so visual edits, were never really, it's not like we ever sort of planned them. didn't really, it's not like they were like a roadmap item that needed to be prioritized. They'd kind of just always been on the horizon since day one, because it just felt intuitive to us that you'll always want to directly manipulate software.

And so that's kind of why, why we did them. And then when we built them, I mean, we actually built two versions of them almost. So the very, very first version that we built our kind of in-going hypothesis was that design tools have solved a bunch of problems. And really what we're adding uniquely is the ability to collaborate with AI and manipulate the outcome in a known

Nad (19:07.072)
And so the first version that we built was actually like super familiar to anyone that has used any of Photoshop, Sketch, Figma, Insert Design Tool here over the last 20, 30 years. So we had a layers panel where you could, you know, browse all of your layers. We had a properties panel where you could, you know, inspect things and then manipulate them. All the good stuff. But we had this moment where we realized that actually these things haven't really moved since the 90s.

And so the very first version of Photoshop had a layers panel in like, think, 1992 or something like that. And so we started to sort of ask ourselves from first principles, like why haven't things evolved? And we thought there was a good reason for like previous shifts. Like, you know, if you look at like a desktop to web, it kind of makes sense. Like you still have a desktop computer, so a desktop interface makes sense. But what we realized was that actually now with AI, we think we can move forward.

like genuinely forward rather than iteratively. And so what we did is we actually, deleted the layers panel because we realized that like who cares about layers. Like I think the fact that there's even such a debate amongst designers about like who names or doesn't name your layers. It's like, it's, that's such a leading indicator that like, do we actually care about this?

Ridd (20:20.933)
Naming or not, yeah. Don't delete my group 1427.

Nad (20:28.586)
Yeah, exactly. So we built a layer panel, we got rid of it, we built more styling, we got rid of it. Even down to, so I'm quite technical, so I don't know, I know Flexbox quite well, for example. And so in a tool like Webflow, I'm quite at home if I want to be like, use justify between at this responsive break point or whatever, it gives me more control. But we just had this revelation, we were like, who wants to learn Flexbox?

Like who wants to sit down and be like, I'm going to ingest all of this crazy domain knowledge in order to just create something that I like and create something that I want other people to like. And so, yeah, so we basically built this sort of design tool version first, had an existential breakdown, deleted half of it, and then shipped this kind of simpler version afterwards. And so the simpler version basically linchpins on

rests on, we're trying to find this tension where, like, when do you want to manipulate things directly versus when is it actually just better to use AI? And so we're trying to find, you know, find these moments or these key interactions where natural language is superior versus when natural language is inferior. And so most of the design process was indexing around, was trying to find those lines.

Ridd (21:48.863)
Did you actually ship the full layer panels to even like a beta or was it just internally you had this sense that this is not the direction that we should go?

Nad (21:58.665)
For that one specifically, was internally. That was like we built it and we used it and then we slept on it and then we woke up the next day and we were just like,

Ridd (22:07.719)
Yeah. The grand reveal of the next morning. Do you still like it or not?

Nad (22:13.71)
Yeah.

Ridd (22:15.857)
Even, I wanna keep going even deeper because even within this new smaller contained ballpark of like, okay, we don't want the full layers panel, but we still wanna find the right level of affordances to give users to make these more precision changes. What were some of the things that you were wrestling with as a designer even figuring out how to implement that version?

Nad (22:43.468)
Yeah, so I think the word that the team got really, really bored of hearing from me was progressive disclosure. And so we were basically just trying to figure out like, do we show and when and how do we do it progressively? so yeah, like where we landed was basically a single panel where first of all, the feature is like almost invisible. Like if you're not a designer,

and you are never going to care about manually setting a color palette for your app or whatever, you probably won't even notice that the button exists in our interface. And that was very deliberate because actually, not everyone is a designer as well. a lot of our users as well are people building apps for the first time. And so first of all, the entire feature is completely hidden. And secondly, it gets more progressively complex once you drill down into more advanced properties.

And so that was, most of the work was figuring out, okay, like how should we be progressive over time?

Ridd (23:46.72)
Do you have any thoughts on where this could go or are you viewing visual edits as a building block for any future explorations? How are you thinking about that?

Nad (23:59.535)
Yeah, for sure. mean, I think coming back to when I was saying that, you know, we think the best that we think that, I'll start again, sort of coming back to this idea that the best tool is completely instant. We see like a lot more value in just continuing to build this out. And so the eventual goal will be to have something where you have as fine grained pixel level control as you can get from a fully fledged design tool.

Where I'm less certain is will the shape be design tools as we know it? Just because I think there's an opportunity to declare a lot of what we've got used to as legacy. And that's, like, that's, think, where we'll probably experiment a lot more. It's where we'll probably, you know, get a few things more wrong before we get things, a few things more right. It's where perhaps people might feel a bit more frustrated because this thing's just plainly missing. Like if you do want to name a layer, you can't just...

you know, one click go. But I think with maybe like a one or two year view, I think it's the right thing to do, like rather than just sleepwalking into, you know, assuming that we need the tools of the past in the future.

Ridd (25:07.955)
Yeah. It's not just the tools of the past though. Like you're in a really fascinating space and I basically never ask about competitors on this show, but I think I am going to ask you if that's okay because I mean, you're just in this unprecedented little

Nad (25:20.462)
You

Ridd (25:24.319)
collection of companies where you're not the only young rocket ship even everything's moving so fast all eyes are on this suite of products so how do you think about the right level to even pay attention to what's happening around you as a designer at one of these companies?

Nad (25:40.141)
Yeah, I mean, so first of all, I'd say it's really fun, as in like working in tech in this space right now is as fun as, you know, if I feel as energized as I did when I was a kid, like doing this for the very, very first time. So that's really, really great. What's less great is it can be super distracting. Like even just, I don't know, even just scrolling over Twitter whilst having a coffee.

Ridd (25:55.838)
Awesome.

Nad (26:08.654)
or like whatever, there is like, there are thousands of things that can suck you in. And so like that's, that's a bit of a personal battle. So I've had to like up my like, I don't know, my phone lives on like, do not disturb 24 seven, because my life is better that way. And, you know, I try not to, I try to time box a lot for anything that could be a distraction. But yeah, but it's super energizing, honestly, it's, it's, it feels like

And I can only say this with hindsight, it felt like things got little bit stagnant. Like we kind of had mobile and obviously that was a huge shift. And then, you know, as a designer, then we started to think about, you know, designing cross-platform and things like design ops. But we kind of understood SaaS, right? It was like, of course there was going to be new SaaS companies, but it was what it was. It's like, okay, deliver some value.

Ridd (26:58.751)
Totally.

Nad (27:05.71)
charge people for it a recurring basis, like more or less. And now everything's changing. And I think that's awesome. so, like, yeah, ultimately it's a super fun, super energy.

Ridd (27:17.855)
Do have any beliefs or hypotheses about the future of the state of design tooling that you're kind of working backwards from as a designer?

Nad (27:27.374)
So I think the future will be, I think the same way that developers have, I'll start again. So I think the same way that developers have their own development environments. Like if you look at IDEs, like the I stands for independent. And the reason why every development environment can be independent is because code is interoperable, right? It's like you can have your source code, store it somewhere. Developers can pick and choose how they want to work individually, per device even, and everything just works.

And I think the future of design will be really, similar. And so I think there's going to be multiple winners. Like I don't really see it, see there being like, there'll be one AI design tool that will win. Likewise, I don't even see it that, you know, the incumbents are like the best positioned. think there'll be, I can imagine almost niche tools for niche purposes, like depending on whether it's motion or doing more detailed color work or using shaders or like whatever it might be.

But I think now with LLMs, like code can be the source of truth rather than design files. And I think that's going to enable this interoperability and therefore design tools being able to work independently but contribute to the same source.

Ridd (28:35.977)
Yeah, I think it even goes back to some of the emphasis on learning and curiosity that you were talking about earlier. Like it's the first time in so long that there's a real fracturing of the market and maybe we're inning one and I think we are but

Gosh, mean, all we talked about was Figma for a long time, like many years. And I do believe that they're going to make some kind of a play. And you know, we have config here in a couple months and everyone has their ideas of what that could look like. But the fact is there are a lot of really interesting niche tools and a lot of different ways that designers can visualize their ideas now, which is very exciting.

Nad (29:11.886)
100%. And I think also like, I think niche tools should be like celebrated. Like I think in tech, in venture capital, like the name of the game is always like, who's going to win. And it's always like, who can get like majority market share. But especially now with AI, that we can write software cheaper, I think we should be celebrating the fact that we can create sort of more like single purpose tools that can focus on one problem and doing that really, really well.

Ridd (29:40.16)
Have you played with Unicorn Studio out of curiosity? Like that's like the perfect example of a niche tool for me where it's like no code WebGL and there's not that many people tinkering with it but the people that are are are just making the most incredible output on Twitter is obviously like where I'm seeing it and it just, I look at something like that and I'm like, man, I'm so excited for the long tail of tooling.

Nad (30:03.224)
For the, for the, so I haven't played around with it, so for the uneducated, like what's the, like what is it? And like what should I do? Like what should the first thing I do be if I play around with it?

Ridd (30:12.543)
So that's the thing is it's like it's so art forward because it's just open-ended web GL where you can create these really really detailed 3d motion effects and then it exports a Format that you can embed as like a framework component for instance and so like one of the things I helped with is like making this 3d moving orb, but it's all controlled in code, you know, it's not a video file and so it's a

It raises the ceiling for what you can do with these crazy visual details. Maybe in a similar way that something like Rive would for animation. I'm a tooling nerd, so this is just a fun time to be someone who does spend too much time scrolling on Twitter getting distracted.

Nad (30:56.942)
Cool. You've added one distraction to my list.

Ridd (31:01.407)
Yeah, speaking of distractions, actually, I do want to get nerdy for a second here because I was looking at your roadmap and I saw MCP in the next up column, which is one of those kind of buzzwords that you're seeing all the time on Twitter now. And I don't know, I'm sure other people that have come across it feel the same FOMO that I do. So do you have the ability to explain what that might mean or what it might unlock for designers in the future?

Nad (31:31.661)
Yeah, so MCP stands for model context protocol and in typical computer scientist fashion, it's a terrible name. Like we are terrible at naming things generally. So all it is, is it's just a standardized way for models to talk to other things. And so if you're building with AI, you're able to integrate MCP and anything else that integrates MCP will just be able to interoperate. And so we're using MCP right now.

something that we're cooking up at Lovable where we'll be integrating with MCP servers on things like Stripe, as well as things like web scrapers, as well as SuperBase, which we use for building full stack applications. Where because we've done one integration with MCP, Lovable will just interoperate with all of these things really, really well. And so what we'll see is we'll go from this world of like, don't know, LLMs being little silos where they have their own

history, their own knowledge, and that's kind of self-contained and separately one particular SaaS platform being its own silo over there as well, to just all of these things being able to talk to each other. So that's the dream. That's the pitch. Pretty bleeding edge though. And I think there's also a lot of promises being made that actually maybe aren't quite being met yet. And so we'll see where this goes, but it's super exciting.

Ridd (32:54.207)
Can we talk about the super base piece for a second? Because that was actually my aha moment with lovable was when I could just connect it to a database, talk to the database and make changes without having to get into the schemas or really understand how anything's actually working behind the scenes.

What was that like designing that integration and even more broadly creating interactions that try to simplify and demystify some of the technical things that are happening behind the scenes? How do you figure out where that line of abstraction versus control exists for users?

Nad (33:30.871)
Yeah. so the super base integration, we, we made it because we, we had this kind of deep fundamental belief that, that most like most people, so again, like we, we integrated super base because we, we wanted to enable people to create full stack applications. And so before Laveable existed, there was like multiple options to create like a landing page, static website or whatever.

super difficult to create like a real working application. And so we looked at a bunch of different options and we really, really liked what C for Base was doing. And so it's a bit of a no brainer to use that or to enable people to have to use that for a backend. And sort of how we designed it, we basically shipped the simplest, smallest version of it that we could. And then we just sort of

We did two different things after that. The first thing is we added to it very, very slowly with a bunch of user onboarding calls. So we had it in private beta for a while, and then we would onboard people into it one by one. And then just simply, just like classic iterative product development. That was one thing that really surprised us actually with all of this was that people are really willing to go on a

like quite a long self-education journey with these tools. And so I think like classical thinking has been this whole sort of don't make me think and sort of like reduce friction, reduce friction. But what we're seeing is that people are very stimulated. And so like people can do things that they never could do before. They're doing things that they could never even imagine before. And actually what's happening is that as soon as people get a taste of like, wow, I can actually do this for myself, they're willing to go on this entire self-education journey of

Like, oh, let me go and I don't let me learn what about databases even like, don't know what one is. Like I'm going to Google what is a database. I'm going to sit on YouTube for like two hours learning about what like a managed backend is or whatever it might be. And so in terms of where we landed, we had these early indicators that people felt very empowered by being able to create full stack. And we also had this early indication that people were willing to educate. so in the end.

Nad (35:55.917)
We actually cared less about like, what is the technical abstraction and like, what is jargon? Because jargon is quite like individually dependent, depending on your domain knowledge. And so I think we've struck an okay balance so far of kind of just explaining what it is and the value of it, and then trying to hold your hand at sort of key moments. But I think we can do a lot more. And so like, we're kind of like very, we're kind of right, right in the middle at the moment of just like, to be a little bit technical, but not too technical.

Ridd (36:26.503)
It makes sense what you're saying about like the getting a little taste because that's just my experience. You've been reflecting back on the journey. It's like you get so much value and you're you're so interested in that first like 10 seconds. The first time you generate anything, you're like, holy smokes, that was crazy. Let's do it again. And right away, you're very motivated to keep

Going I guess and I don't know like I blinked in the next thing I'm like reading Twilio Docs because I want to hook up the API You know like I had no intention of doing this, but it's addicting You know it's it's just fun to try to solve the next problem, and then the next problem the next problem

Nad (36:53.546)
Hahaha

Nad (37:00.92)
Yeah, a hundred percent. it's like, think, I think fun is the word. Like we, we think a lot about flow. And so, you know, I mean, as, as a, designers, we know this, right? Like, you know, when you're in flow and you know, when like, you almost lose all, you know, concept of time. and really like, one of our kind of driving philosophies is just trying to figure out what promotes and what detracts flow. And so when we think about things that way, it's actually quite surprising, like how.

Like how many technical concepts or how many technical abstractions, you know, might initially seem like they're quite domain specific, but if they're promoting flow and if they're empowering you as you build, it's still super fun. And so that feels like a good outcome for us.

Ridd (37:46.698)
talked about promoting flow, speed to feedback. It's clear that you do have these philosophies as this team that are guiding you. so are there any other that we have not talked about that are kind of serving as your North star as a kind of serving as like a North star for you as a designer.

Nad (38:05.326)
One thing we talk about a lot is clock speed or this idea of clock speed. And so we think that we build the best product by learning as much as possible, always. And we think we learn as much as possible by kind of having an uncomfortably high clock speed, like individually and as a team. And so we try to challenge ourselves on, you know, how long do we take to make a specific decision?

this communication need to take us long, like rather than, you know, arriving at a conclusion and being like, let me sense check that with someone else and put in a meeting for next week. Like what stops you from making a, like a 10 second version of that decision on the spot instead. And so we challenge ourselves on clock speed a lot. And that, I think that's paid dividends when it comes to like overall learning on our capabilities and like what we can build. It comes with the, the kind of trade-off that

you sometimes that can come in the face, that scrappiness can come in the face of quality. But so far, I mean, that's basically given us a super powerful product that people love with really, really great fit where I'd rather have the sort of quality challenge of like quality can always be better than and with some fit rather than the other way around.

Ridd (39:22.623)
Is there an example where you've prioritized clock speed and just pulled the trigger on a decision versus turning it into this debate internally?

Nad (39:31.065)
Honestly, probably every major feature that we shipped. like the visual edits, for example, I for sure we had this philosophical debate on like layers panels and like, let's see if we have a shot at making these legacy. But it was also like, okay, there's one path where we simmer on this for days to weeks more. There's another path where we just remove it from the conversation and we can get new feedback uncomfortably fast.

And so I guess we're trying to embrace that uncomfortable part of uncomfortably fast.

Ridd (40:07.283)
I feel some conviction because I've been using the word simmer a lot lately as I work on a new product. Let's talk about your personal process a little bit more. When are you reaching for lovable in your own design journey?

Nad (40:24.322)
Yeah, so I, and this is very subjective, like very personal. So in general with, with design, like I, I always start kind of big to small. And so I'm very much like, okay, like hierarchy first information within that, and then content design. And then once I'm happy with content, then lay it out. And so in terms of my design process, I try to ask the big questions first. I try to figure out what I want from a content perspective. And then depending on.

what the feature is, I'll either reach for Figma to figure out the best way to lay out the information, or if it's interactive, like these days I just go straight for lovable. And sort of, I think where I was getting frustrated by design tools was just the whole like pool noodling of like needing 500 artboards with like the most perfect sort of puzzle of like orchestrate orchestration in order to, you know, build what I wanted. Whereas now I just generally will design maybe the first state in Figma.

And then punch out to lovable and then just make an interactive from that. And so I'll kind of jam with the AI to work through like live prototypes.

Ridd (41:33.503)
Can you talk a little bit about what jamming with the AI looks like for you and any lessons or tips that you've picked up along the way to help designers become better at prompting?

Nad (41:43.503)
I would say treat AI as a creative partner. It's surprisingly good. you know, if you've, I don't know, if you do any, in any other creative discipline, like experimentation is always good. Like actually a lack of structure is where you find, you know, where you find novel solutions. And so rather than thinking, okay, I need to have the structure and the perfect idea. And I need to sort of translate that for this AI to then execute on what I think is in my head.

Just be like super open and like just jam with it the same way. I don't know if you're like a musician and you're just jamming with someone, like just go for it and like things will just happen. And like this is, you know, this is the same as like if a photographer, like a photographer doesn't try to manipulate light perfectly, they set up a shot and the shot is in the right direction. But you know, nature provides some light and you know, the photons bounce around in an unexpected way. And then, you know, at some point something beautiful happens and like, that's when you're like, okay, I've got it. And just treat designing with AI the exact same way.

I'd say like obviously you need to exercise your own taste and you need to apply your own filter on everything that happens. But I'd say don't expect it to be perfect and don't try to be perfect. Just go with it.

Ridd (42:53.609)
Do you have an example of when collaborating with AI took you to a place that was a little bit unexpected, but it turned out pretty awesome?

Nad (43:00.718)
happens all the time with content design, I'd say. And like sometimes the hallucinations are actually really, great for this as well, especially with like naming features. So yeah, definitely more on the content design front. I'm trying to think of anything interesting on the visual or interaction side. Yeah, actually one thing that I'd really recommend like anyone to do is pick up a

pick up like an AI powered design tool, or a tool like Lovable and actually just feed it different art styles. And so, building UI that you like, it's going to look probably a little bit vanilla to begin with, but as soon as you start to think about adding personality, like actually just ask it to style things for you and almost act like an artistic creative director and go crazy because these models are trained on the entirety of human knowledge. And so if you say something like, make it more art deco.

or make it more Bauhaus or whatever. Like don't stick to the UI styles that you see on Twitter of like, don't know, Glassmorphic or like whatever. Like think of anything visual and they do a surprisingly good job. And so yeah, just treating it as a creative collaborator, like not just on the functional parts, but everything else is like super, it can be super rewarding.

Ridd (44:23.763)
I love that. You're totally right. There's a lexicon of adjectives that relate to UI and I almost exclusively use those when I'm interfacing with AI about like a set of visuals. That's such a great piece of advice. Just breaking out, like I can say anything. I can say anything and it's gonna generate something. So I might as well use that as a way to break out of the box of what I'm capable of imagining.

Nad (44:48.194)
Yeah, 100%. And like one thing, when we were working on, we didn't shift any of this, but when we were working on like auto generating color scales, like I was feeding in a lot of, I'm a big like cinematography nerd, so I was feeding in like a lot of stills from some of my favorite films and some of my favorite cinematographers. And so you could even be like, I don't know, like build a UI and then be like, hey, like here's a shot from like, like my favorite, like where's Anderson's flick? And like, let's make this feel more Anderson. And like it,

does a surprisingly good job. It's super fun.

Ridd (45:21.897)
How much of a role as a designer at Lovable are you playing in shaping the interactions that users are having with the AI, the specific words that are coming out, any like system prompt stuff versus the interface itself? Is that part of the role for you?

Nad (45:35.469)
Yeah, it's both. I started out on the interface side, so of course, the first problem to solve was let's put together our UI that people are going to interact with. But you kind of quickly realize that setting the line height of the AI response isn't really designing AI. What people do with it kind of is.

Ridd (46:00.253)
Hahaha

Nad (46:02.318)
So yeah, for sure. we have, we have a, it's pretty, I'd say it's pretty meritocratic internally in terms of the way that we build our AI, like everybody in the edit, everybody in the company can edit like how it thinks and how it works. And so actually most people in the company contribute to it and even like, like non-engineers. And so if there is, I'm trying to think of an example, like for example, one of the people who works on our support, like they're contributing to the core AI.

all of the time and they're sort of closing the loop from, you know, what would typically be a customer service problem to just, you know, feeding back to the AI to just improve things like on the spot. And we have that feedback loop there as well.

Ridd (46:44.671)
It's not the first time I've heard it where people on like support or growth teams are contributing back to like the core system prompts. And I think it's a really interesting trend where I was kind of mentioning this earlier, like companies fall into two buckets right now. You have companies that are adapting to AI and you have companies that have been birthed from AI and AI and its capabilities are at the center of how they work and how they operate, how they think.

I'm wondering how much that resonates and if there are other examples where you can kind of point to the way that the org operates at lovable that is distinct and unique from what you've experienced in the past because of the because of the fact that lovable is an AI native team.

Nad (47:28.462)
Yeah, so I think almost every bit of people infrastructure that we've got used to creating, I think it's a bit challenging in general. And I don't mean to be too alarmist with that. It's just the reality of what I'm seeing. And not just across Lovable as well, by the way. There's other companies, also much larger, that are doing this AI-first pivot and seeing this as well. So in Europe, like Klana.

quite famously is doing this and also intercom as well have been pretty public about doing this kind of pivot. And so I think entire functions can collapse and merge, which is really interesting. At my last company, we had so many people that sat between product and customers where they were almost just different flavors of the same problem. So we would have product managers and researchers.

and solutions architects and pre-sales engineers and account managers. And this kind of laundry list of people where the job was like, you know, know the product and know the customer, but solve a different part of, you know, different parts of this flow. And so that's like a really good example of like, okay, you could collapse almost all of that down to, you know, either one function or like very few people. And I've seen that across the board, like entirely. And so I think we have the benefit as a new company of like,

rather than having to pivot all of this to the new world. We can just stop. But I for sure think it's the future and kind of where things are going.

Ridd (49:03.263)
How does the value proposition of design shift in that new world?

Nad (49:09.218)
So I think...

I think, I mean, the obvious thing that everyone says is that, you know, like taste is going to be paramount. I think that's a hundred percent true. The other thing that I find really interesting and I've, I've thought about this for years and I'd love to get your perspective as well is I find it interesting when different industries use the term design in different ways. And so for example, I'm a huge Formula One nut and I love like motorsports. I also love like aerospace and like the chief most engineer.

in those industries is the chief designer. And so like, why is it that all of these other industries, like being a designer is just so fundamentally different to being, you know, what we call a designer in tech. And so I think we'll see more of those, more of that merger. And so I think design and engineering is quite an obvious one, but actually, in a lot of ways, I think they are two sides of the same coin. And so now with the advent of AI, I think that can merge in sort of very, very new and exciting ways.

as well as cross-functionally in other ways, like say design and product management for sure.

Ridd (50:17.917)
Yeah, that was the piece that I was going to add on where even going back to what you were talking about in the very beginning where you're sitting in between the founder and the market. That's designed at a very high level. It's positioning as design. No. How do I want to design the shape of the entire product offering and how does that fit into the different opportunities that I'm seeing? And I'm excited in a world where, yeah, we can even.

further increase the speed of iteration and more people are capable of shipping and getting something out the door. That part of design is exciting to me too, where it's like the very strategic product level design, market level design.

Exciting to think about.

Nad (51:01.23)
Yeah, a hundred percent. And I think it's all to play for as well at the moment. think like if I, it's, it's maybe like easy to forget that tech is quite young. Like we've literally gone from like, I don't know, websites in the nineties to like web 2.0 to like, here we are. And, and there's a lot of like management practices or a lot of like company structure things that we just sort of made organically. And like, it's not.

the way we've arrived at organically isn't because it's the most optimal design, it's just because it's kind of just what happened incidentally. And I think the other thing that's really easy to forget is that, I mean, one of the reasons why I love tech is that there's almost no barriers to what you can do. But the other side of that is that we also end up with bad managers, like frankly, like we end up with people who are like, not trained or like not, they maybe like shouldn't be in that position. And this also extends to like founders in a lot of ways as well. And so

means that we build functions and entire companies around quite imperfect or suboptimal structures as well. And so I think all of it's up for play at the moment. so whatever we've considered traditionally of product design and engineering and these sort of kind of formal lines between them, I think we can blur if not eradicate as much as possible.

Ridd (52:25.471)
Can we speak to someone who's listening, who is excited about everything you're saying? Conceptually, it makes sense. And yet there's still this chasm that they're having to cross to figure out like, how does a tool like Lovable fit into my everyday workflow at working at a company that isn't pushing the boundaries of AI? They're probably still working on that SaaS. And it's like, okay, like, but where does a tool like Lovable sit into my process? And how can I even think about using it to push my craft forward?

Nad (52:56.172)
Yeah, I mean, there's also the reality that it might not, might just not be the fit as well. So, you know, there are other tools. So for example, we don't support, importing. If you have an existing application, you can't bring that in and then edit it. but what I would say is coming back to this, this idea of like constant learning, like you learn so much by shipping, end to end. so if you are non-technical, as in you're not an engineer who can, you know,

develop, build, deploy, maintain full-stack applications. You can do that now for anything you want. And so just even the sheer act of solving something that feels like a small problem to you, you can build it, you can ship it, you can give it to people and you can learn from it. And that in itself, I think is incredibly rewarding and will reveal, you're going to learn things and you're going to reveal more about yourself even.

think, yeah, I would encourage people to play with it from that perspective. It's just, and don't, even if you're not, I don't know, commercially minded, even if you're not thinking like, I want to start my own startup or I want to do X, Y, and Z, just do it for fun. Like the same way that you would, I don't know, make a loved one, like a home cooked meal, like just make a loved one an act and just, just see what happens.

Ridd (54:17.215)
started making birthday cards in Lovable. made one for my dad where it's like, can deliver it. I make a QR code and that's the card and then you scan the card and then it's custom website with little fun little animations and it's like, why not? It's fun.

Nad (54:20.639)
Nice.

Nad (54:34.072)
That's awesome. And do they like them as well?

Ridd (54:37.151)
So yeah, it's great. It's totally unique, totally unique. It doesn't even take that much time, you know, but it's just a fun way to be creative. I've started lowering the bar basically for what I can make. I made like a, my first foray into super bass was a Super Bowl, like.

betting game where I asked like 20 questions for the most popular Super Bowl prop bets. And then everyone filled it out and then it would generate like a dynamic leaderboard and you could see who got the most questions right. And we could all watch together and refresh on the page. And it's like, it was amazing. Like would have never been able to do that before. It took me probably two and a half hours and it was some of the most fun I've had in months.

Nad (55:17.358)
That's awesome. And I love those two examples as well because I'd actually blocked this out of my memory, like whenever I like going back almost like 10, 15 years, I used to send greeting cards online to people because that was a dumb thing, but they were always riddled with ads. They were horrible. And so like, it's so good, but now you can just build something completely bespoke. It's yours. And we just don't even have to think about that.

Ridd (55:33.777)
Yeah, so bad.

Ridd (55:43.71)
Yeah. right, so we were touching on some of the like AI native org, everything's up for grabs. How are you then reacting to that as someone who's, you you kind of had this blank slate of a design org to assemble. How does that impact the types of designers you're looking for, the traits that you want to prioritize, and even the way that you dream about how you all might work in the future?

Nad (56:10.542)
So I think one of the things that's unique at Lovable is that we hire probably more generalists than companies do generally. so like we actually, most of the team, well maybe not most of the team, a good portion of the team is ex-founders. I'd say one thing that the entire team has in common is that everyone's really high agency. And so generally people have had like, I don't know, slightly unusual backgrounds in some way, shape or form.

And so for example, Henrik, who runs our social media accounts, he kind of got into social media because he used to run a, uh, an Instagram account for the office, like the U S office that went completely viral, hundreds of thousands of followers. He started like monetizing it as like a teenager with like merchandise and stuff like that. And so he just like really deeply understands, um, like understand social media and has this kind of maverick streak about him. And so.

Ridd (56:49.86)
no way.

Nad (57:06.858)
We on the design side, like we're basically thinking about things the same way of like hiring or finding people who are like generalists, very high agency, like don't necessarily think too much about like, okay, here's the constraint of the box that I fit into. And also in some way have this kind of maverick streak of, you know, just figuring things out for themselves.

Ridd (57:33.129)
I love the culture of former founders. That's about as fun as it gets in terms of generalists, everybody's wearing all the hats, we're all just figuring this out together. I gotta imagine this probably makes for a fun place to work.

Nad (57:45.103)
Yeah, for sure. this, I mean, the nice thing is that especially as a designer, it's not like, design is not waterfall here. So it's not like here's the perfect designs. I've thought through every single edge case, like here you go. It means that we can collaborate and calibrate on kind of the most important parts, which is, know, what problems are we solving and why, and like, what's the overall philosophy and like, really like sort of nail out more of the happy paths together. So that's, that's super rewarding in itself.

But also just working with, you know, lot of high agency individuals, like everyone's just super smart and like super driven. so, yeah, like the opportunity again for learning is just huge, which is great.

Ridd (58:28.287)
Any rituals or, I don't wanna say processes, any other defining trait, I don't wanna ask this. Basically I'm gonna give you a catch-all to just talk about.

You know what, I guess even just pausing off the record, is there anything on your mind that we just haven't talked about that you definitely wanted to come up before we kind of land the plane?

Nad (58:53.122)
Bye.

Nad (58:58.83)
through my notes.

Nad (59:06.67)
So we didn't really talk about designing for AI specifically, because I think one thing I want to talk about is, I mean, if you think it's interesting as well, is just what it means to, I guess we talked about design for AI earlier. There's one aspect that we didn't touch on, which is that the best AI solutions have this kind of symbiotic relationship across the user, the models, like the models context. Okay. Okay.

Ridd (59:30.983)
Okay, pause. I'm gonna ask you a question. I it's great. I already can tell where it's going. Okay.

Ridd (59:40.285)
Any other challenges or considerations that you're experiencing when designing for AI products specifically that maybe someone who's not in this type of field would be unaware of?

Nad (59:52.419)
Yes, I think one of the things that really, really surprised me is that there's a completely kind of symbiotic relationship between the end user, the models, the context that the models have, and also how you build around the models, like with the actual architecture of your own application as well. And this needs to work really, really well across the whole stack. so really kind of less abstract examples would be for like lovable users, if you're trying to add a new feature to your app.

The way that we handle that is through like one entire code path and one entire model path, which is really different to if you're trying to fix a bug. And so I think in a lot of, one failure would be if we treated these things as like technical problems where it's more like, the AI engineers are going to figure out what the AI, what context the AI models will have in these specific instances. And wherever we've succeeded, it's actually been a user experience problem. It's been, okay, like what is the user trying to do in that exact moment?

What is their goal even before they launched the app? how, how are they breaking down like tasks in terms of how big they are or how small they are and like, how are they navigating through that? And I think the best AI products that I've, that I've used are the best solutions really, really nail this sort of marriage of user goals to the individual implementations. And so I was really surprised at how symbiotic all of that is. And so actually whilst we had a wait list, so we had a wait list for around

six to nine months before we did our kind big public launch, we did like three major re-architectures where we almost deleted the entire app and started out again. And it's because we weren't kind of happy with the core user flow, like this sort of core flow that users were going through as they were iterating on their apps. And we couldn't just edit the UX on one hand and think about AI on the other. We had to think about these things completely together.

Ridd (01:01:47.712)
But it makes sense why it's so important to have things exist in code because it's like the distance between the user experience and what exists in a static mock has never been wider.

Nad (01:02:00.728)
Yeah, 100%.

Ridd (01:02:06.623)
Before I let you go, we've covered a lot of ground. Any parting ideas or advice or learnings that you want to leave people with who are interested in how you all are working as a team or even just what it's like to start to tinker and explore with AI?

Nad (01:02:26.636)
Yeah, mean, I'd love to, I'd actually love to learn from others as well. so like, I, I think there's so much up for grabs right now that there's, you know, a few key products out there that are doing like really amazing work. And I'd love to sort of figure out like, like who, which are the best AI products out there right now. And like, what, like, what is getting everyone else excited? Like we spoke briefly about granola, like granola's turned how I think about even like note taking like upside down.

Ridd (01:02:53.599)
Totally.

Nad (01:02:54.766)
And so like anything where there's like an interesting intersection of like users can actually behave in a different way now, thanks to, you know, products existing, would love to hear about.

Ridd (01:03:07.249)
anything that's already on your list that you're taking inspiration from.

Nad (01:03:11.394)
I think granola is a really, really interesting one because the thing I love about granola as well is that the UX is so minimal. It's like four or five small decisions made really, really well. And then that just empowers like a bunch of different use cases. And it also forces you to change in a lot of ways. And I think actually historically, like we've always said, reduce friction and sort of meet users where they are. Whereas with AI, we kind of need to invert that.

And it's not about meeting people where they are, it's about giving them superpowers. And Grinnell is one of those tools where I feel in lot of ways like I have superpowers.

Ridd (01:03:49.13)
Well, I've definitely felt that about Lovable too. Even just like using the mobile site in a cafe, like it just has become the new game that I play on my phone. So I appreciate all of the work that's went into it and you taking the time to share a little behind the scenes with us today.

Nad (01:04:04.878)
Great, I know you have real pleasure to meet and to talk.

Ridd (01:04:11.071)
I'm.

