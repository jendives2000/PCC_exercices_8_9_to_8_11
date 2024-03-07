
# WHAT I LEARNT

---

## Icecream bug

I've been using "**icecream**" for a couple of days now, exclusively on "replit.com" though.  
When I pip installed it on my new virtual environment (anaconda) on VScode, **it installed it but I couldn't use it**.  

So I searched a solution on Claude.ai, on Google (reddit and github) and after going back and forth like that for a long couple of hours, **I found the solutions. **

Turns out there are packages ready and available in Anaconda, and "icecream" is installed from some of them.  
The thing is "icecream" is installed with other modules, like "executing" (I know, strange name for a module, right?).  

And the other thing is that **"icecream" needs to be installed from the "forge package"**, using this command `conda install conda-forge::icecream` **BUT** this does not install "executing" from that same package.  
And this resulted in installing an **obsolete version of "executing"**. 

The solution was to **initially install it from the forge package too**:  `conda install conda-forge::executing`. 

I wrote a comment in the github page (links below) where they helped me figure this out. I wrote it because no comments was really relevant to my specific case. 

---

## Passing a List through Functions

These 3 short exercises were part of the chapter 8 related to **Functions**.  

When passing a list through functions the `.pop()` method comes handy (*line 43*). It takes out a value from the list and also **permits the assignment of it to another variable.**
The `remove()` or `del` methods do not permit it. 

Then, the `.append(message_out)` method actually moves the value to the new list, iteratively through a while and a nested for loops (*lines 40 and 41*). 

--- 

## How did I Do?

The author of the book from which I got these exercises made the solutions available online (links below).  So **I was able to check my work** and see if I did well or not, and potentially improve or explain my mistakes. 

Turns out I did pretty well, my code is not a true 100% copy of the solutions as it is now but essentially it is, at around 95% I'd say, **with tiny improvements on my parts, IMHO**.  

I think **my version has a better readability**, due to:
- **comments that are referencing a numbered list** of comments (helps in rolling out the code via a split screens layout **on the first read**)
- my variable name '**message_out**' is to me better than what he suggests: 'current_message'
- my **function declaration has 1 parameter instead of 2** in the solutions. This **does not make the code more obscure**.
- on line 41, instead of a default placeholder (_) I initially used 'message' but the problem is that it'd be unused anyway. **So using the underscore _ signals that. **

### Commits & Branch

Because I didn't need to correct my work I didn't need to branch out on my github repo.  
So I just did commits on the exercises until I finished them. 

--- 

#### Resources:
Python Crash Course #rd Ed. [solutions to exercises 8-8 to 8-10](https://ehmatthes.github.io/pcc_3e/solutions/chapter_8/#8-9-messages)  
Anaconda [forge package & icecream](https://anaconda.org/conda-forge/icecream)  
Github [Icecream issues page](https://github.com/gruns/icecream/issues/79)
