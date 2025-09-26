# Dive Club Interview: Figma Make Team (Holly Li & Niko Vetter)
## Episode Notes
**Host:** Ridd  
**Guests:** Holly Li (PM, Figma) & Niko Vetter (PM, Figma)  
**Topics:** Figma Make, AI Prototyping, Code Integration, Design Process Evolution  

---

Ridd (00:00.174)
Maybe this starts with Nico and taps into your perspective - you've worked on prototyping for so many years and seen all the technological advancements. How has the introduction of Figma Make evolved the way that you think about what a prototype even is?

Niko (00:26.433)
The fascinating moment to me was at Config London. I was there with Holly and a couple others preparing for different keynote demos. Holly pulled out a couple of demos we had built internally, and one was from Tammy, one of our designers - a full 3D modeling environment.

There was this moment where I looked at this and thought, how are we not more crazy about all of this happening? I've worked on prototyping for the last seven and a half years. Over the years, we always made incremental improvements - smart animate, interactive components, small fidelity improvements.

Then AI and code comes along and makes all of this progress feel miniature. We got used to the fact that it's possible to create a 3D modeling environment in Figma Make. That's ridiculous.

Hard problems are gonna stay hard problems. I've worked on stuff where you just try to explain it to someone and you have a hunch, but you can't really put words to it yet. You don't even know what the way of evaluating your problem is.

AI will help you express your first idea, and Figma Make will help you build a first prototype faster. But as a designer, you'll still have to do that a lot of times until you find the right solution. Hard problems are going to stay hard.

Ridd (02:40.268)
It wasn't that long ago we were talking about how cool variables were. I was playing an interactive 3D game where I was fighting off aliens in Figma Make before this call.

Niko (03:04.041)
It makes you think, what were we doing back then? The beauty is that the high level goal always was to get thought and expression closer together. AI and code in this industry has made significant progress on if you have an idea and you can start to express it, you actually can get really, really far.

---

Ridd (03:44.398)
I don't want people to think that Figma Make is always the right tool for every job. How should designers think about the types of prototyping formats and when to reach for what?

Holly Li (04:03.362)
What's very notable is that Nico worked on the former version of prototyping and is also working now on Make. The DNA of prototyping is very important to us - we're taking a very design-centric way of building out tools for designers.

Because Make is so accessible - all it takes is an existing Figma design or just an idea you want to articulate in two to three sentences - our goal is to add that into a designer's arsenal when it wasn't an option before.

It's worth noting that two thirds of Figma users are not designers. There's a huge population of folks that are more native in ideas and sketches, but now have their own mechanism for prototyping that wasn't as easy before.

Niko (06:00.533)
We just launched Code Layers a couple weeks ago as the first time the Make technology is integrated into an environment designers are more intuitively at home with. One of the biggest questions was: how do we get code and AI in a way that feels intuitive to designers?

Sometimes you don't want to create an entire prototype from scratch. Maybe you already have stuff and want to extend it with just one interactive element. That's what we brought Make into Sites as Code Layers.

There's a Slack thread with 400+ replies about how we should integrate code into a design tool in a way that fits designers' needs for iteration, exploration and alignment. Code is generally about components first, don't repeat yourself. But what do designers expect when they duplicate a code layer?

---

Ridd (08:04.766)
You said "extension" that I appreciate. There's this straw man that AI just creates generic slop. Nothing I make with prototyping tools looks like AI because I'm trying to recreate my exact designs. It's still rooted in what I bring as a designer.

Holly Li (08:54.24)
One thing we feel strongly about with Make is that it's brought to you by the same ethos of Figma - understanding that designers are the source of creativity. We encourage you to start with a design. Have Make work off your design as a collaborator instead of showing up empty-handed.

We're finding that designers have these really large and messy canvases, and Make can be an additional way to take those designs multiple frames at a time, bring them to life, and show those prototypes as part of design crit. Starting with the designer's work is really important.

---

Ridd (10:24.866)
I want to get specific about workflow. I'm someone who makes a big mess - my Figma files look like the Charlie Day meme. I'm prototyping in real time. I don't treat prototyping as something I do once I have the design figured out. One challenge is knowing when to make the jump to Make, because there's upfront effort required.

Niko (12:04.653)
The answer is it depends. Sometimes you start with something where you think you can describe how this works but can't imagine what a UI should be - then you start with words in Make.

But sometimes I can't describe it. I have a vague sense and have to feel my way through it. I have to create a design by hand, put things on there, create duplications, and slowly illuminate the room like fog of war in computer games.

Then I find the rules and descriptions for how this should work. Maybe that's when I describe it back into Make. We're at version one - it's our role to blur those lines more like we did with Code Layers.

The design process flips entirely on its head. If you have an idea how it should work but don't know how it should look, start with Make. If you know what it should look like but not how it should behave, start with designing and put it back into Make.

Holly Li (13:45.234)
These AI tools are introducing new ways of validation. I've literally told Make to use colored boxes to represent elements and show me how something would swing in when I click, just to make sure the mechanics make sense before sketching it out.

You could show up with a hyper-specific dashboard designed down to the button, bring that alive in Make and fixate on a button hover interaction. It explodes the surface area for the types of questions people can validate at any point in their process.

Ridd (14:12.567)
You're prompting Make to keep things at wireframe level?

Holly Li (14:15.789)
Yeah, I've said "keep everything as gray boxes" and "I just want to see when I drag this box, how the movement of other boxes will change." Just to validate the liquid movement. Once I validated that it works in code and feels good, then I figure out the design specifics.

Niko (14:35.432)
There's mechanics, visual parts, information architecture, edge cases. Whatever is most important for your product, that's what you need to focus on prototyping as early as possible.

It's not linear low fidelity to high fidelity. The prototype Holly described with gray boxes - visually it's low fidelity, but in interaction design, it's really high fidelity. Previously it was sketch on paper, then wireframe. But maybe the moment where you make something interactive is when your problem is pulling in real data and seeing how users react.

---

Ridd (15:23.789)
I was prototyping suggested follow-ups in a chat UI. The quality of the interaction is everything - either it feels good or feels bad. I'm not great at interaction design, but that's actually a feature when using Make because I can use language that doesn't map to CSS or Framer Motion. I just say "make it feel kind of like this" and something happens that I wouldn't have had the language to communicate to an engineer.

Niko (16:01.234)
When we last talked, we were discussing advanced prototyping with triggers, variables, conditionals. We basically built a programming environment visually. But it was still hard.

Now you can ask it to make something "bouncy like a rubber ball on a rainy afternoon" and it figures it out. We're meeting users where their head is at instead of getting them to meet where the computer is at. You have a sensibility for interactions but don't have the language to describe it at the computer level. That's the beauty of AI generating code.

Holly Li (16:45.567)
We're seeing designers build interaction playgrounds in their Makes - "give me a bouncing toggle, sliding toggle" with controls to adjust speed and Bezier curves. They're using Make in a meta way to nail the exact degree of interactions, building interaction tools within Makes to compare different speeds and behaviors.

---

Ridd (17:12.345)
After I get something interesting, I was like "add an inspect tab and break down all the logic for developers." Then "make it so you can one-click copy CSS for these gradients." I'm building my own inspect tool inside my prototype to send to developers.

Niko (17:30.123)
What are we even doing as design tool authors if you can design your own inspect panel?

Ridd (17:35.678)
Are there other slam dunk use cases you've seen where Make just makes sense?

Holly Li (17:42.456)
Designers are using Make in two tracks. One is "help me prototype exactly what I have today." The other is "help me break the bounds of what we're doing today by 10%, then 20%." They have dedicated teams using Make in those two different ways.

We're also seeing a lot of AI chat UI work. As products adopt AI as core UX, there's chat and dynamic interactions, non-deterministic layouts. You can't get close enough with stills.

---

Ridd (18:23.789)
At a demo day in San Francisco, 11 or 12 of 14 companies had AI chat. That's the pattern of the era. If you're getting feedback on anything that happens dynamically with AI, you can't do it unless you're sending a link that behaves like the end product.

Holly Li (18:45.234)
At Config London we showed using a chatbot with an API key - an AI DJ live - prototyping how that chat looks on a music player with a "chatty or concise" slider. That actually works and it's incredible.

Niko (19:01.567)
You can access the device's native behaviors. You're not constrained to what we built interfaces for in Figma design. You can ask it to generate code and access native camera, gyro sensor - all at your disposal under the surface.

---

Ridd (19:34.789)
How are you seeing this evolve collaboration and the design process at the team level?

Holly Li (19:42.345)
Designers are excited about both increased speed to show concepts and new ease at exploring fringe ideas they never had time or ability to do before. We're seeing both prototyping existing designs faster and exploring new design directions at increasing velocity.

PMs are also hugely excited about Make. They no longer feel they need to wait for a designer to get something done and polished before they can weigh in. They want prototyping and early product exploration to be a key new part of their remit as a PM.

Ridd (20:15.678)
Is that why you switched roles, Nico?

Niko (20:18.234)
Good ideas can come from anyone. We need anyone to be able to express their ideas. We launched VR and I've been astonished with illustrations where people are creating things that were theoretically possible but are so wonderful.

Different people have different views on software. It's our job to create a platform where they can collaborate well. When we had Code Layers in internal betas, people were creating elements for Sites. Then we surfaced it as a Make file and people started asking much bigger questions because they're clicking "new make" and presented with an input field.

If you duplicate a code layer and somebody has chatted with it, you see the entire chat history. It's closer to a group chat than a single AI chat. We enable collaborative code editing as well - developers can support designers writing code. It's a full blown code editor inside Figma.

---

Holly Li (21:45.789)
I can give a tangible example of how I used Make to build Make. We had a huge offsite with big brains trying to figure out the future of a specific roadmap part that was very abstract - "moving X to Y, flattening A to B." People with PhDs couldn't follow what was going on.

I went to Make and basically wrote down the PRD. I pasted in existing Make UI and said "allow me to do this capability, be as opinionated as you want on UI." Within three back-and-forth messages, I had something I shared with the crew that let us visually grok what happens. It took less than five minutes.

Ridd (22:23.456)
The goal isn't being correct - you might be fundamentally wrong, but you've given people something tangible to point at and be like "I hate it for these reasons." You've made progress.

Holly Li (22:35.123)
We also launched Style Context, which allows you to add a library to your Makes. It extracts CSS, fonts, critical styles and appends them to a global.css file. Even when exploring ideas without designs, this creates foundational aesthetic consistency with your products.

---

Ridd (23:12.789)
Secretly, I'm most happy about being rewarded for being organized - my libraries, auto layout, habitual layer naming. All of that is the most valuable context for the model.

Holly Li (23:25.456)
You're ahead of the curve.

Niko (23:27.234)
Maybe that's why I became a PM now.

Holly Li (23:29.567)
Nico's poor design hygiene.

Ridd (23:32.123)
Where might this be headed in terms of impact on the industry, role of design, defensibility of the role?

Niko (23:40.789)
Defensibility is maybe the wrong word - it feels like "this is my little kingdom." Since we've talked about different qualities of software, ideally we build a space where different qualities can be worked on by different people good at those qualities.

You're not good at interaction design, I'm not good at visual design. We should work together. AI and code is glue that brings us closer together rather than creating a unicorn designer doing everything alone.

Design is about alignment, figuring out the 999 ways not to do it. Hard problems stay hard. Details still matter. You describe something, get a functional version, then there's 15 more small questions, then 30 more. Details have to be decided for things to feel intuitive.

We'll see more collaboration, more interactive patterns as ways of sharing things out. Designers have been doing this by hand, figuring out edge cases. So have developers in a different way. AI and code will be glue pulling people together.

Ridd (24:45.123)
I love "code as the glue" because it's the standard. The only way to standardize output within a software team is code, because code is what ships. The only way to all contribute to the same thing is playing in code.

Holly Li (25:01.456)
As we look to the future, Make lives in the context of FigJam, Slides, Dev Mode, Draw. Not only designers use Figma, but PMs, UX researchers, marketers, developers. There's so much surface area where we can show up at moments that matter most for any type of person at any point of workflow.

We're excited to see how Make becomes that accessible way of standardizing what it means to be part of the product and design process, lowering barriers for people.

Ridd (25:34.789)
I'm excited to see where you take it. Thank you for coming on and hashing it out, giving us a glimpse into what you're observing. This has been a lot of fun.

Niko (25:45.234)
Thank you for having us. I'm sure we'll be back for a third time talking about prototyping again.

Ridd (25:51.567)
At the rate of change, I don't anticipate we'll have to wait long.