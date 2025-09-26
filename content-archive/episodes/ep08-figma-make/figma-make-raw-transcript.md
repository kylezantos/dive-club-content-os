Ridd (00:00.174)
to high level.

And maybe this starts with Nico and it's kind of tapping into your perspective a little bit of have you worked on this for so many years? You know, like you've seen all of the iterations of prototyping and all of the technological advancements. So how has the introduction of Figma make evolved the way that you think about what a prototype even is?

Niko (00:26.433)
Yeah, I think the fascinating moment to me was at Config London. I was there with Holly and a couple others and we were of preparing for different keynote demos. And it was cool kind of like seeing everyone there playing with the stuff. And then Holly kind of like pulled out a couple of the demos that we had built internally ahead of the keynote. And one of them was from Tammy, one of our designers, a full 3D modeling environment.

And it's just like, and I think there was this moment where like, I looked at this and we're like, how are we not like, like more crazy about all of this happening? Because it's like, like, again, like I've worked on prototyping for the last seven and a half years. And I think over the years, we always made incremental improvements. had smart animate here, we added interactive components. We, we added all these kinds of like small fidelity improvements.

Ridd (01:05.613)
Yeah.

Niko (01:21.843)
And then AI and code comes along and makes all of this progress feel like miniature. And already we kind of got used to that, that that's possible. Like it's possible to create a 3D modeling environment in Figma Make. Like that's ridiculous. And I think that from there, kind of like, of course, the whole question is like, what does this mean for designers? What does this mean for the role of design? And I think there's one part that I keep coming back to is that

Ridd (01:38.307)
Yeah.

Niko (01:51.873)
hard problems are gonna stay hard problems, right? I've worked on stuff where you just try to explain it to someone and you just have a hunch, but you can't really like put words to it yet, right? You don't even know what the like way of evaluating your problem is. So you're gonna end up like tapping in the dark in a way, trying to find a solution that somehow works and like you can't put words to it yet. And I think that like

That's still true. And AI will help you express your first idea, of course, and Figma Make will help you build a first prototype faster. But as a designer, you'll still have to do that a lot of times until you find the right solution. Hard problems are going to stay hard.

Ridd (02:35.896)
Mm-hmm.

Ridd (02:40.268)
It's funny because it wasn't that long ago that we were having a conversation on this show and we were talking about how cool variables were and reducing the number of frames and cutting into the noodles. And like, was just clicking on the community demos before this call and I was playing an interactive 3d game where I was fighting off these aliens and it was all in figma make. And it's like, my God.

Niko (03:04.041)
Right? Like it makes you think of like, did we like, what were we doing back then? A little bit. Like, and I can, I can, I can of joke about it because it's literally my own work that I'm looking at. And I'm like, what was I doing there? And I think it's like, I think it's the beauty though of all of this is that it, it ultimately the, the high level goal always was to, get it close to, to get thought and expression closer together. And, and we've gotten, we've been like this AI and code in this industry has made

Ridd (03:08.895)
Yeah, it's crazy. Yeah.

Niko (03:32.521)
significant progress on if you have an idea and you can start to express it, you actually can get really, really far. And that's amazing.

Ridd (03:44.398)
It's not, like I don't want people to think that Figma Make is always, every single time, the right tool for the job though. So, like how should designers even think about the types of prototyping formats? Like what's your strategy for what to reach for and when?

Holly Li (04:03.362)
I maybe I can take a stab at this at a high level, is for one, mean, I think it's funny to hear, you you two reminisce on the former conversation you had about prototyping together. Those are the old days. The sweet days. I think that what's very notable here is that like, it's interesting that Nico, you know, worked on that version and is also working now on Make. And so,

the DNA of prototyping essentially is like, you know, it's very important to us that like we are taking a very design centric way of building out tools for designers for these types of use cases. And so to answer your question around, you know, what type of tool make is, I think the really beautiful thing about it is that because it's so accessible,

because all it takes is like an existing Figma design you have, or even just like idea that you wanna articulate in two to three sentences and you can bring it to life in a way. Our goal, I think is just to add that into a designer's arsenal and just make that an option when it wasn't one before. And it's worth also noting that two thirds of Figma users are not designers. And so there's a huge population of folks.

that are maybe a little bit more native in ideas and in sketches, but now also have their own kind of mechanism for prototyping and idea production that didn't, you know, that like wasn't as easy to them before. And we're really, really excited about essentially the Cambrian explosion of creativity and ideas that will come out because of, you know, the introduction of something like Make.

Niko (05:55.553)
I think the.

Ridd (05:56.992)
It's just go. Yeah.

Niko (06:00.533)
And I think the other side too is we just launched or just a couple of weeks ago launched Code Layers as like the first time the make technology is actually integrated into an environment in which designers are more like intuitively at home, like sites as an open-ended canvas, right? And one of the biggest questions there was, how do we get code and AI in a way that feels intuitive to designers as a way that it extends their workflow, right? If you think about make as something that

like is really good at creating the entire prototype from scratch. Sometimes you don't want to create the entire thing. Maybe you already have a bunch of stuff and you want to extend it with just this one element here to be more interactive. And that's something that like we brought make into sites as code layers. And the biggest discussion here with a lot of the engineers was, wait, this is, we're bringing code into a canvas based design tool. How do we do that?

And I'm not kidding. There's a Slack thread. We actually talked about this at config in one of our deep dives. There's a Slack thread with 400 replies, 400 plus replies that went on over multiple days because we were talking about how should we integrate code into a design tool in a way that fits to designers like needs for iteration, exploration and alignment. Whereas code generally, because it's generally used for production is

Ridd (07:03.438)
god.

Niko (07:26.013)
is more about like, don't repeat yourself components first. Right. And so the biggest discussion was I create a code layer and I duplicate it. Do I get another version of this or do I get an instance of this? Because under the hood, it's a React component. Right. So what, engineering uses as terms for, for code inside of a design tool and what designers use for this didn't really match. And there was a lot of discussion going on on how, how we can make this work for designers.

but also have a system under the hood that is like actually a solid foundation for how code works within a design tool.

Ridd (08:04.766)
Yeah. You said a word extension that I really appreciate because there's almost this straw man that I see in the design community from people who are a little bit less excited to adopt code-based explorations in that, well, know, AI just creates this generic slop. And it's like, well, yeah, like if you're maybe don't have the design skills and you come in and you just type those three sentences, it's probably going to look like AI, but

Nothing that I make with prototyping tools looks like AI because I'm trying to recreate the pixels exactly as I've made them in Figma. Like they're my designs. And so having that extra level to my explorations, but it's still rooted in what I'm bringing to the table as a designer was definitely an aha moment in terms of how you are positioning the feature.

Holly Li (08:54.24)
Yeah, and just to add to that, think one thing that we feel super, super strongly about with Make is that it is brought to you by the same ethos and spirit of Figma, which is the understanding and appreciation that designers are the source of creativity. And so one of the key parts of Figma makes kind of value proposition.

is extension of your design process. Meaning when you're done, when you have a design, you can just copy and paste it into make. We kind of like really encourage you to start with a design. Have make kind of go off of your design and kind of work with AIs as a collaborator instead of, know, just showing up kind of empty handed. And that way we have found that it

kind of complements the designer's workflow a lot better. We showed a lot of this at config, but we're finding that designers have these really, really kind of large and messy canvases, and that we're excited about the way that make can just be an additional way that you can take those designs multiple frames at a time, bring them to life and make, and then be able to show those prototypes as part of your design crit.

starting with the designer's work is really, really important.

Ridd (10:24.866)
I want to get ultra specific and I'm talk about my workflow, but I know that I'm not alone. And I'll let you know, one of the things that I'm wrestling with as someone who is like the rest of the industry, trying to figure out how do I make sense of where these AI tools and new capabilities fit into how I operate. And I'm a designer who per usual, I like to make a big mess, right? My FIGMA files look like the Charlie day meme. It's absolutely absurd.

But I'm prototyping in real time. don't treat prototyping as this thing that I do once I have the design figured out. I have my monitor here. I'm making a mess. I'm playing with little interactions and I have the prototype mode on my computer. And I'm like, okay, yeah, I don't like how that feels. Let's do, let's try something else, you know? So it's like very much intertwined this act of putting pixels onto the canvas and then seeing how they feel. And one of the challenges for me has been at what point do I make the jump?

Right? Cause like it is a jump and once you operate, once you, once you go into make land, there's a little bit of upfront effort that's required to like get it up to speed and you know, at the point where it feels real. And so it's like, there's still kind of this line in the sand. And sometimes it's, I don't know if it's like at the very beginning of my process or at the very end of my process. And there's not even really a question there, but I,

hope that people listening resonate with it because that's one of the things that I'm really trying to figure out is like, when do I start using these tools? When does it make sense?

Ridd (12:02.83)
Good luck.

Niko (12:04.653)
I think the answer is it depends, honestly. And I think there's two parts to this. On one side, it of course depends on how you intuitively express your idea at first. Sometimes you start with something where it's like, I think I can describe how this works. And I can't imagine what a UI or what a behavior for this should be.

then you're starting with words and then you should start and make, right? But sometimes I've been at other problems where I literally cannot describe it. have to like, I have a vague sense in my head, right? Of like, I think if we do this this way and then you click on this one, then I, and in those moments, the only thing I can do is like feel my way through it, if that makes sense. And I have to create a design.

Ridd (12:58.881)
Totally.

Niko (13:02.207)
by hand, put the things on there, and then create a duplication of that. And I see basically be like, OK, if I click on this one, then I go here, and then I click on something else, and then I go to this other state. And then slowly, I'm kind of like illuminating the room, it's kind of like this fog of war that you see in computer games kind of clears up as I'm uncovering the different states that this thing should be in. Then I suddenly find

Ridd (13:23.918)
Mm-hmm.

Niko (13:28.565)
the rules and systems or the descriptions for how this should work. And maybe that's the moment in which I kind of like try to then describe it back into make, right? And so I think those are the types of things where there's different ways of expressing your idea. And like we're at version one of make and Figma design, right? And it's our role to blur those lines more like we did with code layers and insights as a first step. But yeah, you shouldn't.

have to have this feeling of, now I'm switching roles, I'm switching tools, I'm going into this other world. It should feel a lot more integrated in a way that you can express in the way that makes the most sense for the problem that is right in front of you. And throughout the design process, that changes. The problem right in front of you is always a different one. There's always a slightly different one. Sometimes you have to go into vector editing mode.

or draw a little icon to kind of like see if that helps the communication of your idea better than a make prototype. But sometimes it's the interaction flow. And then you want to kind of like explore what a higher fidelity interactivity piece should be. So I think the biggest thing to me is that all of this flips the design process that we've kind of like seen in the industry. We've talked about this last time too of like I'm designing and then I'm prototyping entirely on its head.

Because if you have an idea just how it should work, but you don't know how it should look like, start with the make, right? If you know what it should look like, but you're not sure yet what, it should behave, start with just designing and then put it back into make. And I think that like, it depends on what's exactly ahead of you. And we need to, it's our responsibility to make it fluid.

Ridd (15:04.696)
Mm-hmm.

Holly Li (15:21.14)
Yeah, just one thing on that, which is like, I think there's two pieces of that answer, which I just want to highlight. The first is like, as Niko mentioned, we're really, really excited and there's a lot of work to be done to make and Figma feel, and your existing Figma workflows feel more seamless. So much really, really exciting stuff that we're thinking about and working through there.

to kind of really motivated by questions like the one you just posed to us. And then the second piece though is just kind of at a more meta level. I think that these AI tools are also introducing kind of new ways of validation and new ways of like thinking through a design process. Meaning, Nico gave a really great example of like, if you don't really know how something's going to work, maybe you wanna prototype it first.

And like what I've literally done before is I don't even have the designs yet, but I tell make like use colored boxes to represent X and just show me at a high level, like how would this thing kind of like swing in when I click blank just to make sure the mechanics make sense in my head before I go to actually sketching it out. And I think that, and then on the kind of other end of the fidelity spectrum, you could show up with a hyper, hyper specific dashboard that you've designed down to the button.

Ridd (16:18.797)
Mm-hmm.

Holly Li (16:48.226)
bring that alive in make and just fixate on like a button hover interaction and you could do that too. And the reason why I'm really excited about this is because like it really just explodes the surface area for the types of questions that people can start to validate at any point in their process. I also don't want to, you know, like I would want to make sure people realize that with tools like make, you can be really, really creative about, you know, at what

stage you're exploring. And it can be the wireframe stuff as well. So just really excited to see what, know, how users use it. And we're already seeing a lot of really, really creative ways.

Ridd (17:30.478)
Just to clarify, so you are prompting make to say, keep this at a wireframe level. I don't want this to feel high fidelity. I'm only going to experiment with the interaction design.

Holly Li (17:41.482)
Yeah, like I've, I've, I feel like I've, I've had examples where, I literally say, keep everything as gray boxes. and I just want to see, like, when I like drag this box, like, how was the movement of the other boxes going to change? Right. And just like to, validate, for example, like a, I don't even have the right words to describe it, but like the liquid movement of how the other things are going to move around this thing as I drag it. and you can keep those as, yeah, I've literally said just like, keep them as gray boxes.

Ridd (17:48.067)
Wow.

Ridd (18:05.57)
Mm-hmm.

Holly Li (18:10.922)
I just want to figure out what this interaction is going to look like. And then once I validated that that could work, like that, that, works in code, that feels good for me to use. Then I will go and like actually figure out like the, the design specifics.

Niko (18:28.243)
It's like, there's, really like what you, what you said is like mechanics, right? I think there's like, there's so many different dimensions of quality of software, right? There's like the mechanics, which I think covers a lot of stuff around like interaction behaviors, maybe some animation details, right? There's kind of like the, there's the visual parts, of course, there's information architecture. There's also the, like the edge cases, how does it react when kind of like data comes in, right? And, and you can ask make to pull in real data and into a prototype. And I think the part is that.

Whatever is most important for you or for your product, that's the part that you need to focus on prioritizing prototyping as early as possible. And again, right, it's not a linear low fidelity to high fidelity, right? Because if you zoom out the prototype that Holly just described with gray boxes, is it a high fidelity prototype or a low fidelity prototype? Because visually, it's low fidelity, but into action design, it's actually really high fidelity.

Ridd (19:20.908)
Yeah, yeah, that's

Ridd (19:26.966)
Really high fidelity, yeah.

Niko (19:28.105)
Really have, so that's kind of like by this one linearity fidelity thing I've always struggled with. And it's like, that just doesn't make any sense. Right. And it's, it's, it's more like a, like a, like a skill chart, right? You want your design to be good in all of those skills, but, previously it's like, I'm going to sketch on paper. Then I'm to sketch a wire frame. But maybe that's the moment where you make something interactive because, because maybe the thing that your, your problem ahead, ahead of you is actually pulling in real data and seeing how users react.

Ridd (19:35.043)
Mm-hmm.

Niko (19:58.497)
to that real data. And that's more important maybe than the visual style, because maybe the visual style is a native iOS representation. You're not gonna design and explore visual stats. You're gonna design how the data comes in and how users react to this. And that's the thing you're designing.

Ridd (20:18.862)
I really like thinking about different axes of fidelity. And it reminds me, even the other day, I was prototyping a suggested follow-ups action inside of this chat UI. And it's very simple UI. It looks exactly like what you're picturing in your head. It's very simple. But the quality of the interaction is everything. Either the design is good because it feels good or it feels bad. Therefore, it is bad. And so playing with that,

was really only possible using code prototypes. But also on that, you described it as like the skill chart, right? I'm not really great at interaction design. I can hold my own, but I don't even have the ability to articulate what I want necessarily. And I've come to realize that that's actually a feature, not a bug when you're in a tool like make, because I can use language that doesn't really even map.

to CSS or framer motion or anything like that. It's just like, make it feel kind of like this. And then something happens. I'm like, that was cool. I didn't think of that. Well, actually, maybe can you take it a little bit further and go like this instead? So I'm creating really fun interactions for the first time that previously, not only did I not have the skills to be able to make, but I wouldn't have even had the language to communicate to an engineer to try something like that.

Niko (21:44.019)
And especially like that's something I've been, it's been so interesting to me because we, when we last were here, we were talking about advanced prototyping, right? And it's about, here's a trigger and you can use variables and there's a set of actions you can do and you can have conditionals and you can check those things. we're like, yeah, we just built a programming environment, like visually, right? But it still was hard, right? And

Ridd (22:03.054)
Yeah. You made me teach like thousands of designers if then statements. spent a whole summer figuring out how to teach it and now we're going to make.

Niko (22:09.46)
I know, I know.

And now you can ask it like, make this bouncy like a rubber ball on a rainy afternoon. And it somehow figures it out and gives you something that like maps to this expression. I think that's, think the cool thing about this is we're meeting users where their head is at, right? Instead of getting them to meet where the computer is at. And I think that's such a big flip in how people express interactive behaviors and any of these.

Ridd (22:30.232)
Hmm.

Niko (22:42.017)
other dimensions of software rather than visual. And that's, I think that's beautiful because like you clearly have a sensibility, you have a sensibility for the interactions you want and the interactions that feel good. You don't have to language to describe it at the computer level, but that's the beauty. That's what the beauty of of AI generating code for you is because it takes in like truly natural language of a bouncy ball when I click on this button and that we can make that work.

And that's, I think, that's nice. I'm really excited to see what happens.

Ridd (23:15.959)
Yeah.

Holly Li (23:17.515)
One thing I just want to add anecdotally, which is think super, super cool, is again talking about how you're not maybe a professional interaction designer. A lot of folks who are using Make are not, but one really interesting observation that we've seen from users is that so many Makes are actually, building in essentially interaction playgrounds in their Makes.

We're seeing a lot of examples where designers are prompting like, give me a bouncing toggle, give me a sliding toggle, give me a this toggle, give me a bunch of different controls to control the speed of the bounce and the Bezier curve of the bounce and yada yada, because they're not proficient designers in CSS kind of like hover interactions or X or Y or Z. And they're using make in a meta way to essentially nail the exact

degree and detail of a bunch of different interactions. And they're doing it also, they're basically building interaction tools within their makes so that they can compare A, B, like how does it look like to bounce at this speed versus to slide at this speed? And it's as easy as literally like prompting make to add those toggles. We actually had one of our demos at config London was a designer had built like a 3D credit card rendering.

and had built all of these different controls around shimmer and speed and X and Y and Z, and then also asked Make to generate then the code for all of those kind of, generate the code once he had kind of nailed those interactions that he could then just like copy and paste. And so again, like very, very meta ways of bringing in entirely different capabilities to your design. And it just comes down to how creative you are with Make.

Ridd (25:02.627)
Mm-hmm.

Ridd (25:14.134)
on the generating the code piece, something that I did actually right before you all released Femime make that it kind of just worked. And I've brought it into my practice of how I use these prototypes now is after I get it to the point where I have something interesting and this one, I was working through some theming logic and it wasn't as much like interaction level code. was very much so like, how does this system work? Because there's a lot of conditional things happening. And, and so I was like, okay, cool. This works now.

And I was like, okay, I'm going to send a developer this link. How do I communicate this? And I was like, add a inspect tab at the top and break down exactly all of the logic and format it for developers. And then I was like, sick, it just worked. And I just sent them the link. And then I was like, Oh, I was like, there's a bunch of this array of gradients. Make it so you can one click copy the CSS for those gradients. I'm literally just building my own inspect tool inside of my prototype to send to a developer. That was a

aha moment for me where I was like, oh my God, can literally do anything.

Niko (26:14.271)
Like what are even we doing as design tool authors, right? If you can just design your own inspect panel, right?

Ridd (26:20.684)
Yeah. Totally bespoke. Yeah. man. Can we talk more about, can we talk about more examples? Like I want to get into your heads as the people that are doing a bunch of user research and seeing how people are using this out in the wild. And again, I know there's people listening that are like, all right, I know that I should be doing something, but I still don't exactly know what I should be doing. So are there other slam dunk use cases that you've seen where you're like, yeah.

I it just makes so much sense if you're working on this type of thing or at this type of stage or in this type of situation, Figma Make is going to be the way.

Holly Li (27:00.128)
Yeah, I can share some examples that we're really excited about. mean, we're in kind of conversations with users every single day and learning from them. And especially at kind of like larger organizations and large teams, know, that the workflows are completely different than if you're just kind of a freelance designer, et cetera. And, you know, one of those examples is that designers are using make.

to one really fun example is that a designer was saying, I used make to absolutely nail the interaction of this button that I need to add to this product. And then he said he duplicated it. And then he has a version where he's just actually asking make and ideating on crazy, crazy non-design system versions of this button.

And he basically is going to crits with both and using make both to show kind of like the real thing today that it should look like. And then a version where like if we changed and we migrated off of X, Y or Z, this is how it could feel. And we're actually hearing a lot from customers that they are using make in kind of like at least these two tracks. One is like, help me prototype exactly what I have today and then help me like.

break the bounds of what we're doing today by 10 % and then by 20 % and explore kind of like adjacent territory from what we have and that they actually have these dedicated tracks in their workflows now and sometimes even dedicated teams that are using make in those two different ways, which I think is really, really cool.

Ridd (28:50.19)
Did you have anything on that, Nico? Or do want to keep going?

Niko (28:55.615)
I'm trying to find an example that Guy, one of our design managers, built and show it on the phone in a second.

Ridd (29:03.614)
I literally will just pause and wait. don't care unless it's like you think it's gonna take like 10 minutes

Niko (29:05.77)
Yeah, yeah. One second, one second. No, it's not gonna take ten minutes.

Ridd (29:09.932)
Okay. I like the strand. want to keep pulling on the strand, even if there's other examples, Holly. Like I just, I think a lot, I go on Reddit a lot and just to remember how much of a bubble Twitter is and people simply can't come up with use cases, which I find ridiculous, but it's like, it's very dominant. that, I, I, at least in, I don't know what you would refer to that legacy software companies. don't know.

Niko (29:15.657)
Yeah, good.

Ridd (29:37.714)
People are still just like, why do I need this? I'm like, what are you talking about? You have magic. Why would you not want it?

Holly Li (29:42.646)
Yeah, yeah. I have a couple examples maybe after Nikos that we can share of, know, so we can't share customer examples, but I can show some examples of ways that you might, you know, prototype with make for some of those use cases, especially since we just launched a style context feature. So I can talk more about that after Nikos.

Niko (29:45.534)
It's...

Ridd (29:54.603)
Yeah.

Ridd (30:11.15)
Sure, Even in my own practice, I've been thinking about where it's making a lot of sense. And there's an interesting thing happening where more and more products are adopting AI as a core part of their own UX, which naturally lends itself to, okay, there's a lot of chat and dynamic interactions happening and non-deterministic layouts and screens and content. And it's like, well, good luck. If you're gonna try to do that in stills.

good luck, you're not going to be able to get close enough to what your product can become. And so as soon as I'm working on something that has to do with chatter interfacing with the AI, I don't even really spend that much time in the canvas at all. Like I get right into it.

Holly Li (30:55.574)
Yeah, absolutely. While Nico continues to find this, think the designing with chat, AI chat is a huge, huge use case. And again, I think one of the last demos we shared at config is using a chat bot with a API key where I think I'm talking to like an AI DJ live.

and prototyping how that chat looks, how big it is on the top of my music product player and all of these things. And we built out a real time, is it chatty or is it concise slider? And all of that actually works and it's incredible. And even in a world where you could be prototyping that, but also you could put that on a website and now, like,

ship really, really awesome websites with more AI capabilities now with Make as well, which is really cool.

Ridd (31:58.094)
Yeah. I was at a demo day in San Francisco, I guess maybe last month for South Park Commons. There were 14 companies that went up there. And I'm not kidding. bet 11 or 12 of those companies had some sort of AI chat in it. Like you can knock on it all you want, but the reality is like, that's the pattern of the era. And as it becomes increasingly popular, like you have to, you gotta

Holly Li (32:15.83)
Yeah. Yeah.

Ridd (32:26.102)
make it feel real, especially if you're getting feedback on it, right? Like if you're gonna get feedback on anything that happens dynamically with AI, you can't do it unless you are sending a link that behaves and looks and feels like the end product. It makes a lot of sense.

Holly Li (32:43.094)
Speaking of that, Niko's got... You want to walk through this?

Niko (32:46.337)
I got here. Yeah. So.

Ridd (32:47.845)
my gosh. Wait, no, keep doing it. Keep doing it.

Niko (32:52.085)
Yeah, I'm I'm taking a little break. So it's easier to cut. Yeah. One example I've seen that I think is, is shows the power of code with code layers and in make, right. As you can access the device, detailed behaviors, right. And so in this case here, I have one that, gave one of our design managers has built where it uses the gyro sensor of the phone to kind of like, like, like flip through a bunch of these images here. and I think this, shows the, the,

Ridd (32:54.582)
Okay, okay. Yeah.

Niko (33:22.369)
the ability to like ask for anything, right? But also be able to tap into the native material that is code. You're not constrained anymore to what we have built interfaces for in Figma design, essentially, right? But you can ask it to generate code. I have asked it, I don't have the example ready, but I have asked it to kind of like have like a thing where I have to like select five elements and it would send an event.

Basically, I asked it just to like send an event and then I had a little completion bar at the bottom and I had to press those five in rapid succession to complete the bar and kind of like build a little game. And those were like five different code layers that I ended up letting them communicate with each other. Did we have an interface or a feature? Like we've been thinking about something like events, of course, for the longest time, but we don't have a feature for this. I looked into the code and it was just using the JavaScript events feature.

And was just building it for itself. And then I think that like, it's, to what you said earlier with the inspect panel, like building your own inspect panel. Right. I think the beauty of, of, code layers and insights is it's an escape hatch. Right. You can do anything you want, which puts you a little bit into like a decision paralysis as well as like, what the fuck am I going to do now if I can do anything I want. Right. But I think that's kind of like the power there is, is, is just try.

Ridd (34:35.756)
Yeah.

Niko (34:49.953)
try and duplicate a code layer, try out something else and see. yeah, you can, if you publish your code layer or your make, you can access the native camera, you can access driver sensor. All of those things are at your disposal now, which I think is just astonishing that that's just there. It's waiting for you right under the surface of all of these pieces.

Ridd (35:13.902)
We've talked a little bit about how this impacts the individual designer workflow and non-linear workflows. But I kind of want to zoom out for a second. And given all these changes at the individual level, when you're talking to teams that are making use of these new prototyping capabilities, how are you seeing it evolve the way that collaboration happens and how the design process itself has changed even?

Holly Li (35:40.192)
Yeah, I can answer this maybe in two ways. One is starting with the designers. I think what we've heard as I kind of hinted at earlier is that there is excitement around both the increased speed with which they can show concepts, but also the kind of new ease at exploring

kind of like fringe ideas that they never really had the time, bandwidth, or yeah, ability to do before. And so as I mentioned before, we're seeing designers do both prototyping existing kind of designs to bring to crit faster and show kind of the behaviors and also exploring kind of like new design directions at like increasing velocity.

Now, what that means for the change in a design process, think, is it's still early days. But what we're really excited about is that, know, Figma make exists within kind of the existing Figma workflows, meaning that like people are being able to share with their teams, you know, exist, you know, like share with existing teams in the same way. And it's all kind of in that same ecosystem. And then on the other hand, you know, like

PMs and developers are also a huge part of, I think, Figma makes potential. And as we referenced earlier, we're seeing also, actually with a lot of our users, that it's PMs who are being very, very vocal about their excitement and their use now of make in their workflows, meaning that they no longer necessarily feel like they need to.

waits upon a designer to get something done and polish before they can weigh in, that they now, because they have access to Figma designs as well, start being a part of that kind of product design flow and ideation process, both earlier and in an entirely different capacity. So we're hearing pretty loud and clear that a lot of our PMs want to be some of the, you know, want

Holly Li (37:59.746)
prototyping and early product exploration to be basically a key new part of their kind of remit as a PM. And so really, really exciting about what that means for just essentially like the translation and the less effort required between translation among all of the different types of hats on a team.

Ridd (38:28.654)
Is that why you switched roles, Nico?

Niko (38:31.105)
No. I think that like, let's try that again. Let's try that again.

Ridd (38:34.316)
Hehehehehe

Ridd (38:40.934)
Yeah, you're good. good. You're It does. When everybody can contribute in design and code, it does make you kind of wonder like where does PM live and where does design live and Nico, I know you made the switch to PM recently and it's part of me is kind of like, so what? You know?

Niko (39:02.133)
Yeah, I think there's this beauty there where good ideas, that's something we've been talking about at Figma for years, right? Good ideas can come from anyone, right? And we need anyone to be able to express their ideas, depending on however that might happen, right? Like we launched RAW and I've been just astonished with how many people are creating illustrations where I'm looking at them I'm like...

I know that this was theoretically possible now, but this is so wonderful, right? And I think that there's so much from so many other people that they should want or like they should want to express their ideas. And it's beautiful that they can. And I think that that's the part similar to the different axes or different dimensions of qualities. It's different people have different views on software too, right? And I think it's our job to create a platform in which they can collaborate well, right?

And in that case, it's that one thing that has been really, really interesting to me is seeing how people look at code layers within sites and they look at make as essentially a file type right now. And it's the same technology and we surface it as a file type and we surface it as an element that is powered by AI and code, right? And so it's the same technology, but the perception literally by having this in slightly different contexts.

It's wild how it changes how people look at it and how different roles look at it as like, it for them or is it for someone else? Because I think that when we had code layers in our internal betas, of course, or in our internal staging versions, people were kind of like playing with this and we're creating elements for sites, right? And then we surfaced it as like a make file and...

people suddenly started asking it so much bigger questions because now they're going to the file browser and they're clicking new make. And then they're presented with an input field. And then they're starting, their brains go wild and they're starting to ask about all these different possibilities that's there because that's the only thing you can do in make today. And there's a lot of value in having these different kinds of entry points and meeting users where they are with their idea.

Ridd (41:09.304)
Mm-hmm.

Niko (41:23.807)
Right. And, and, and this is again, this is the first version, right. Where we are today. But I think that shows a little bit about the range of, of, of how we can leverage AI and code in different ways. It's not one workflow to rule them all and replace everything you have ever seen. Right. Because as we talked earlier, sometimes you got to feel your way through something and then AI isn't the right job because I can't, I can't fucking describe it yet. What I'm trying to do. I need to just do it and then take a step back and be like,

Ridd (41:50.136)
Mm-hmm.

Niko (41:53.301)
What did I do? I know that this was right or that this was interesting, but I can't describe it to someone else yet. And if I can't describe it to someone else, I can't describe it to the AI on what to repeat there. And sometimes it's the other way around and different users come at it from very different angles. we need to meet them where they are and find ways that the PM can collaborate then with the designer can collaborate with the developer. And one of the things we've built in code layers, right,

is that if you duplicate a code layer and somebody has chatted with it, you see the entire chat history. In a way, it's actually closer to like a group chat than it is to like a single AI chat that I have. And we could be in a design file or in a sites file and you chat and ask the AI something and then I see, it's working now based off of Ritz question. And once it's done, I can ask it a question. And all the while, the other thing we enable this

is collaborative code editing as well. I think that like kind of flew under the radar a little bit, right? But developers can support designers in writing code into the code layers. It's a full blown code editor inside of Figma. Like we also launched that. Like I think that's the part when it comes to collaboration that shows a little bit like you can express your idea by drawing something in sites. You can express your idea by asking the AI to create a code layer.

Ridd (42:54.946)
Yeah. Yeah.

Niko (43:20.233)
Or you can just write code, right? And like you can write code in Figma and that's the small news of the last couple of months. Right. And I think that that shows a little bit that like, depending on who you are, depending on what skills you are, we need to find ways for you to express your ideas.

Holly Li (43:37.622)
Can I, I'd like to give a very tangible example actually of how as a PM, I've actually used make to build make. I can't show you the example visually because it has to do with something that's coming. But I can just, I can describe it at a high level because it actually, touches on so much of what Nico just mentioned. And also like why I think it's like a really

Ridd (43:55.63)
I hear an IPO is coming.

Holly Li (44:06.946)
perfect example of why it make inside Figma is so useful, which is, we had a huge offsite a couple of weeks ago with a lot of big brains in the room trying to come up with the future of a very specific part of our roadmap that was very heady. It was very, very abstract. had to do with like moving X to Y, flattening A to B, then being able to do C on top of D. was like very,

Like people in the room. Yeah, exactly. People in the room with PhDs were like, my God, I cannot follow what is going on. And what does that mean for how the design of this, when we surface this to users is going to look. And, I, we didn't have designs yet, right? This is, this was part of a conversation that happened over two days. And I went to make, and I basically wrote down the PRD. I was like, this is what a user should be able to do. And this is everything at a high level. I.

Niko (44:36.993)
I love that description.

Ridd (44:39.022)
Hehehehehe

Holly Li (45:06.888)
I pasted in the existing make UI and I was like, just allow me to do this capability. You can be as opinionated as you want on the UI. I just need to be able to click on that button to see X to see Y to see Z.

Ridd (45:20.952)
Just to be clarifying here really quickly, you had basically no visual intent inside of that prompt. Okay.

Holly Li (45:28.436)
No, no, just existing make UI as a Figma frame attached. And then like what I needed to be able to do at a high level, what we were trying to evoke out of this, out of this new product direction and, know, make outputted something within, think three back and trip back, back and forth messages that I then shared with the rest of the crew that immediately allowed us to visually grok. that's what happens. Like you can.

You know, do this. I wish I could tell you the specifics, but like you can do this very complex thing and then press that thing and have another very complex thing happen. But here's how it looks visually. And here's what a user might want to do next. It wasn't a meat. It wasn't obvious until we just had a version of it that we looked at. And the crazy thing, RID is that it took less than five minutes. It took less than five minutes. We shared that artifact around, you know, you know, the designs for that maybe look very different today, but the.

Ridd (46:17.4)
Hmm.

Holly Li (46:27.072)
The beautiful thing about it is just like the basics of the workflow we understand. And sometimes I think it really helped kickstart the team on the possibility and like the immediacy of this, because we were looking at it we were playing with it. The prototype was real. You could click that to do X and do Y and do Z and it was live. We played with it.

Ridd (46:47.38)
It's cool too because the goal at that point isn't even being correct. like you might fundamentally be wrong about how it should be implemented, but you've given people something tangible to point at and use and be like, well, I hate it for all of these reasons. Great. We've made progress. We know what we don't like, you know, and sometimes it's very difficult to even get to that point without having something in hand.

Holly Li (47:10.976)
Yeah, exactly. And, you know, I don't necessarily want to take us down this segue if we want to talk about something else. you know, the one thing about you saying it like it wasn't correct, right? Obviously, the code under the hood was just, you know, there to allow us to perform the basic mechanics. But and the UI, you know, like it added like a color button that like

we would never have or X and Y and Z and it didn't look quite right. However, one of the new features we've launched is this new style context feature, which allows you to essentially add a library to your makes. And while it's not pulling components yet, what it is doing is having make extract the CSS, the fonts, a bunch of other really, really critical styles.

and then just adding them and appending them to a global.css file in your make. And so, and I can show you some examples of this. What we're really excited about with that is that even in a world where people are just exploring ideas that they don't have designs for yet, this is essentially creating like a foundational level of aesthetic consistency with the rest of your products, which I actually think is quite important even in the

Ridd (48:35.694)
That's a big deal.

Holly Li (48:36.77)
brainstorming ideation phase that like, this kind of looks like my company. This kind of looks like my brand or my team. Yeah, and I can kind of share some examples right now visually of like how that, you know, how we're excited about it. So, let me.

Ridd (48:48.43)
That'd be great.

Holly Li (48:56.578)
Yeah, so one example is.

So what you're seeing here is that down here I have Colab, which is a library. And it's a design system library that we've extracted. And then I've not attached any designs. I've just said, make me a desktop sign up flow. And this is a pretty opinionated using my Colab icon logo, using the right fonts, the colors.

And it's creating me a signup flow that looks like what that design system might evoke, which is really, really cool. If you ask it to make you a desktop signup flow without a style kind of attached, it's gonna give you black and white boxes and something really, really generic. And this is really powerful that right out of the box, you can start ideating with something that looks like everything else you're.

you know, you're designing and making and Figma. Another just like fun example of this is, you know, I again here in my prompt box, you can see I have Colab as the style and I've attached a completely separate design. And I've just said like, translate this into the Colab style that you have. And again, this is one shot what it looks like. And so just really, yeah.

Niko (50:23.087)
Holly, do you want to, I think you have to switch screens or something. Like I was still seeing the old one. Okay.

Holly Li (50:29.109)
I'm sorry. Yeah. Should I, I'll start over there.

Ridd (50:29.218)
There it is. no, Say that one. Can you just back up a second? Can you back up a second and the last three sentences again, just so I can have.

Holly Li (50:36.066)
Yeah, sorry about that. So one of the other things we're really excited about is here, I've just like attached a completely separate design. And I've just asked it to translate this design into the colab style that again, you can see here I have in my prompt box. And this is just a completely one shot output. And so really, really excited about like the infinite kind of like

translation abilities that this new feature also gives designers, which is like, you know, if you don't have an existing design, you can like now create any, anything you have in your mind in that style. And if you have existing designs, you can now translate them into, you know, infinite different styles that you have, you know, if you use our kind of library extraction feature. And so just really, really stoked about.

even just kind of these like small ways that we're already starting to build out like more and more kind of like fidelity tooling essentially in make to allow the ideation and the prototyping to be even more seamless.

Ridd (51:44.888)
Big deal.

Niko (51:44.893)
And what we're like, we're like two months post config, right? I think that like, it's like, we probably, there's this feeling of like, we're like at config and let's like slow down. Right. Cause it's like, but I think that's the, that's been like the, the, the, the cool part seeing that too, it's just kind of like how rapidly we can just keep going on a lot of these pieces. And I think that that for like, for me, seeing that config moment was, was big because at that point it was like, okay, the stuff is out. Let's, let's go. Right. Cause I feel like in the weeks before we, of course we can't.

Ridd (51:48.515)
Yeah.

Niko (52:14.207)
There has to be one big announcement and now we're going and like, the design system theming is the first. And it's cool. It reminds me of the Studio Ghibli trend that happened where like I'm able to like convert things into another style. it's it's sick.

Ridd (52:27.839)
Mm-hmm.

Hmm. Secretly, the thing that I'm most happy about in terms of the impact that all of this new AI tooling is having is I'm finally being rewarded for being the really organized designer with my libraries, my auto layout, my habitual naming of layers. And all of a sudden that's like the most valuable context for the model. And I'm like, I knew it. Like I knew it. I knew it was going to matter. It does not.

Holly Li (53:00.106)
Yes. my god, you're ahead of the curve.

Niko (53:01.121)
Maybe that's why I became a PM now.

Ridd (53:05.247)
Hahaha

Holly Li (53:07.84)
Nico's poor design hygiene. He's like, can't keep going with this.

Ridd (53:11.95)
just slinging rectangles in groups like it's 2015.

Niko (53:12.001)
I was like, Oh yeah. Oh yeah. Maybe not groups. I wasn't as much as a group designer, but yeah. No, and think the other thing too, like to the examples, right? think like the other thing that we're like, it's also, we're like just like overlooking in a way too. like, I'm pretty sure that all of those checkboxes now worked and all of those sliders were working, right? And like, how nuts is that? They just like all work out of the box and like it does that too.

Ridd (53:20.588)
Okay, good.

Ridd (53:34.19)
Hmm.

Yeah.

Niko (53:40.369)
There's so many aspects here where like, yeah, it converts my designs into functional code and makes it look correct. but it also makes all of those things work. And I think there's so many aspects where like previously in the past, right, we've built in the active components for you having a checkbox. But...

Ridd (53:50.51)
Mm-hmm.

Ridd (54:00.492)
Yeah, the checkbox is the perfect example of when it's like, this is actually like the hardest thing to prototype without code.

Niko (54:06.244)
Yeah. Or like, like the, the radio buttons are really annoying. They're, they're like a checkbox, right? It's two states, but like a radio button group is like, like there are just things that are better in code to describe in code and then behave in code. I think that's where like a lot of the future is going where like you can work with, with, with the material that makes the most sense for the problems at hand. And I think that's just shows this too, that like all of this was good converted. It's, it's working. Right. And that's like, that's, think.

Ridd (54:10.125)
Yeah.

Niko (54:34.689)
Like there's like a small, slow wave of like what this means for designers, for design tools that like we're at the startup and that's pretty exciting.

Ridd (54:47.128)
When you think about what this means, we've obviously covered a lot of the short run stuff. Is there anything rattling around in your brain where you're thinking about where might this be headed? Given the types of things that you're exploring internally. know you can't talk at a feature level, but in terms of the way that it impacts the industry, the role of the design, the role of design, the defensibility of the role in the long run, even anything come to mind there that you want to share with us before I let you both.

Niko (55:16.329)
I wonder, I think defensibility is maybe the wrong word, right? I think because it feels like it's like, this is my little kingdom and I'm going to do it by myself. But since we've talked about these different qualities of software, right? Ideally, we can build a space in which the different qualities of software can be worked on by different people that are good at these qualities of software, right?

what you said, like you're not good at interaction design. I'm not good at visual design, right? We should be able to work together, you know, and like we should be able to kind of like leverage Sigma's entire platform in a way that brings the best of each of our strengths together into a workflow that feels even more collaborative, right? And I think that there's just parts where AI and code in particular is something of like a glue that might bring us closer together rather than create this like

Ridd (55:50.776)
Mm-hmm.

Niko (56:12.901)
unicorn designer who is now doing everything by themselves. So I think that's the part about collaboration that I'm actually really excited about is more people working more together rather than a single person doing it all by themselves. Right. And I think that's important for teams and for enterprises, because in the end, design is about alignment. Design is about figuring out the 999 ways of not to fucking do it. And that's what you need to get to as a team as well.

And then I think the other part is that, I said this earlier, hard problems are going to stay hard, right? The details are still going to matter, right? You can describe something, you get a functional version out of this, and then there's still 15 other small questions and then you answer those and like, it's like a Hydra and there's like 30 more small questions that you need to answer. The details still have to be decided and they still matter for the end user for things to feel intuitive, right? And so I think that the part is that

We're going to see more collaboration. We're going to see more interactive patterns and behaviors as a way to sharing things out. And I think that designers are at the perfect point because they've been doing a lot of this just by hand. They've been figuring out all the edge cases. They've been thinking about all the different ways that certain things do, but so did developers in a different way. That kind of goes full circle to...

going to see more collaboration with AI and code being a glue that pulls people together.

Ridd (57:45.934)
love code as the glue because it's it's glue, but it's also the standard. It's the only way that you can standardize output within a software team because at the end of the day, the coders what ships. And so the only way to all be contributing to the same thing is you have to be playing in code. And if people can do that, then you're right. You can just insert yourself at the point where you are most qualified or most interested. And there's an episode that maybe will ship right before or after this. I'm not actually sure, but I was talking to a designer who

has a motion background and they're working on this animation and instead of doing something in After Effects and then lobbing it over the fence and saying good luck developer, they just started making a shader and it was a way that they could bring that artistic spike that they offer but contribute directly to the thing that the engineer was already working in.

Instead of having that one engineer have to do the full spectrum of output and probably drop the ball on the shader, at least from an art direction standpoint. so code as the glue code as the standardizing layer within a software team is a really, really interesting way of framing that concept.

Holly Li (58:57.376)
Yeah. One, I guess another way of answering that question that touches on it is, you know, as we look to the future, Figma Make lives in the context of also FigJam, Figma Slides, Dev Mode, Draw, all of these other tools and one of the, and not only the other kind of platform, that the platform of Figma,

But also, again, the fact that there are designers in Figma, but the entire rest of your team is there, the PMs, the UX researchers, the marketers, the developers. And so as we look to the future, I think one of the really, really beautiful things that you both have so astutely observed is that there's so much beautiful work and context that lives within Figma and the rest of your team.

And I think one of the really exciting things for make is that that is a lot of surface area where we can show up at the moments that matter most and just be, you know, for any type of person on that team. And at any point of that workflow across any of those products, when is the best time to be, you know, furthering an idea and furthering an idea can mean a lot of different things as we've discussed in this today's session.

And we're just really, really excited to see how make can kind of become that really, really accessible way of kind of standardizing what it means to be part of the product and design process and lowering that barrier for people. So a lot of really, really exciting work that the team is super, super stoked and a lot of exciting stuff planned.

Ridd (01:00:50.914)
I'm excited to see where you take it. And it's not hard to imagine the different ways that it can weave through the rest of the product suite. So I will be buying your IPO and rooting for you as a future stockholder. So thank you for coming on today and just hashing it out, honestly, and talking about all the different ways that this is changing things and giving us a glimpse into what you all are observing in your own research. been honestly just lot of fun. So I appreciate you two taking the time.

Niko (01:01:21.557)
Thank you so much for having us. Glad to be glad to be back. I'm sure we'll be back for a third time about talking about prototyping again.

Holly Li (01:01:23.329)
Thanks, Red.

Ridd (01:01:27.054)
Probably at the rate of change, I anticipate that we will not have to wait long.

