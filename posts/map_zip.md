Since I started programming full time I have improved as a software
developer immensely, I know this because occassionally I'll run into sloppy code,
git blame it, and discover I'd written it six months back!
Even though I can see the improvement, I can also see that Im not broadening
my python toolbox at the same rapid rate as when I was studying for job
interviews, and the reason is simple: my job requires a deep
understanding of our specific system, but not a deep understanding
of the python language. I realized that if I want to get better I need
to do so in my spare time (and luckily we already have a word for that,
practice!)

I thought back to high school and remembered getting better at math by doing
loads of problems from my text book, and wondered whether there was an
equivalent for getting better at python.  Not long after that I
discovered Coding Katas! If you are unfamiliar, Wikipedia describes Coding
Katas as:

> An exercise in programming which helps a programmer hone their skills
> through practice and reptition.

> _Further reading:_ [Wikipedia: Kata](http://en.wikipedia.org/wiki/Kata_%28programming%29)

It turns out there are a ton of sites that offer hundreds of coding katas
to complete, and the one I use is [Code Wars](http://www.codewars.com).
I choose that one because once you solve the kata you can see the best
solutions from other users, which actually teaches you something!

The first problem I solved gave you two lists, one for keys and one for values,
and asked you to write a function that returned a dictionary with the keys paired to the values.
The tricky part was an additional requirement: if there are fewer values
than keys, the excess keys would still go in the dictionary, but paired
to the value None.

Here are two examples that demonstrate the requirements:

    ::python
    keys = ['a', 'b', 'c', 'd']
    values = [1, 2, 3]
    createDict(keys, values) # returns {'a': 1, 'b': 2, 'c': 3, 'd': None}

    keys = ['a', 'b', 'c']
    values = [1, 2, 3, 4]
    createDict(keys, values) # returns {'a': 1, 'b': 2, 'c': 3}

I figured I could do something fancy with dictionary comprehension,
but couldnt get it to work.  I went with the quick and dirty solution
of creating an empty dictionary, looping over the length of the keys list,
and setting the key :value pairs in the dictionary by their respective positions
in each list.  If there was an error, it meant that I ran out of values from
the values list, so I could except it and set that key to None.  The
code worked, and looked like this:

    ::python
    def createDict(keys, values):
        d = {}
        for x in xrange(len(keys)):
            try:
                d[keys[x]] = values[x]
            except Exception:
                d[keys[x]] = None
        return d

I knew this was not the best solution, and after Code Wars accepted my
submission I went straight to the community answers to find the best solution.
It looked like this:

    ::python
    def createDict(keys, values):
        return dict(zip(keys, values)) if len(keys) < len(values) else dict(map(None, keys, values))

A zip and map...I knew these two, Id seen them before, but I didnt
even think to use them! My first coding kata and I already found a tool
I knew of but didnt have in my tool belt.  If you know what zips and maps
are you can stop here (and if you made it this far, thank you for reading :)
If not, I'll briefly explain how the code works.

From the zip function's help page:

    zip(...)
        zip(seq1 [, seq2 [...]]) -> [(seq1[0], seq2[0] ...), (...)]

    Return a list of tuples, where each tuple contains the i-th element
    from each of the argument sequences.  The returned list is truncated
    in length to the length of the shortest argument sequence.

Zip can take two lists and return a list of tuples pairing
the values in the i-th position for each respective list.  Turn this returned
list into a dictionary, and this is perfect for solving the coding kata!
This looks good, but on closer inspection, this only works for cases in which
there are fewer elements in the keys list, which is where the map function comes in.

Fro the map function's help page:

    map(...)
        map(function, sequence[, sequence, ...]) -> list

    Return a list of the results of applying the function to the items of
    the argument sequence(s).  If more than one sequence is given, the
    function is called with an argument list consisting of the corresponding
    item of each sequence, substituting None for missing values when not all
    sequences have the same length.  If the function is None, return a list of
    the items of the sequence (or a list of tuples if more than one sequence).



Again, this looks perect! If you provide map with two lists, the map function
is called with a new list with the corresponding item of each list, and it will
substitue None when the lists dont have the same lenght. If we put None as the function,
and provide two lists, maps returns the list of tuples it would have called
if you had provided a function.  Again, exactly what we need to solve the kata edge case!
Putting zip and math togther, you have a very clean solution.

I hope this helped, I certainly learned something useful and will continue
to use katas to sharpen my coding skills.

