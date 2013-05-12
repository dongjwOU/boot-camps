Software Carpentry Python Workshop.

**Stanford, May 6-7th**


# Testing

## Why testing?

You can skip this session if one of the following applies to you:

1. Your programs never had, and will never have a bug.
1. You/your lab doesn't care if your results are correct, as long as the *look* ok.
1. You prefer to program in an inefficient way.


## Example: Rectangles

You want to study the effects of climate change on agriculture. You have photograph from farms from the 1980's and today, your job is to compare them. As a first step, you need to find where fields overlap in both corresponding photographs. Luckily, your data comes from Saskatchewan, where fields are rectangular.

A previous student from your lab wrote a *python* function **overlap** that finds the overlap of two rectangles. You want to test if the code is correct.

``What what be the test cases that you would run?``

**Task. Find test cases (pairs of rectangles) you want to test the *overlap python function*.**

(The main goal of this exercise is to realize that by thinking about test cases, we are forced to think of boundary cases and exceptions. Like what if the rectangle touch, but don't overlap?)

**Main reasons to test (in this order)**

1. Think about what code should do, in particular in boundary cases.
1. Tests document the expected behaviros (and, unlike comments, are not consistently out of date).
1. Tests give you confidence to change the *implementation* of your code (eg to speed it up), without the fear of braking something that worked before.
1. (Some) confidence the results of your code might be correct.

**Limitations of testing**

1. A 100% test coverage is impossible.
1. Tests measure quality, they don't create it. Ie simply *having* tests in place does not make the code better by itself.
1. If your tests fail, your code has a problem. But if all tests pass, your code might still have a problem.

``In theory, testing should hardly be beneficial at all, but in practice, it almost always is.``

## Nosetests in python

``hands off keyboard - put code in eitherpad for everyone to copy&paste before the exercise.``

This is the file you want to test.

	#Put this in file rectangles.py
	def overlap(red,yellow):
		#Return overlap between two rectangles, or None.
	
		((red_lo_x, red_lo_y), (red_hi_x, red_hi_y)) = red
		((yellow_lo_x, yellow_lo_y), \ 
		(yellow_hi_x, yellow_hi_y)) = yellow
	
		if (red_lo_x >= yellow_hi_x) \ 
			or (red_hi_x <= yellow_lo_x) \ 
			or (red_lo_y >= yellow_hi_x) \ 
			or (red_hi_y <= yellow_lo_y):
			return None
	
		lo_x = max(red_lo_x, yellow_lo_x)
		lo_y = max(red_lo_y, yellow_lo_y)
		hi_x = min(red_hi_x, yellow_hi_x)
		hi_y = min(red_hi_y, yellow_hi_y)

		return ((lo_x, lo_y), (hi_x, hi_y))
	
To write unit tests, create another file.
	#Put this in file test_overlap.py
	from rectangles import overlap
	def test_overlap_with_itself():
		obj=overlap(((0,0),(1,1)),((0,0),(1,1)))
		exp=((0,0),(1,1))
		assert obj==exp

First, we import the function *overlap* form our file *rectangles.py*. Our first test case checks the overlap of the rectangle with lower left corner (0,0) and upper right corner (1,1) with itself. The expected result is the same rectangle. *Assert* checks for a True statement.

To run the test, type the following in the unix shell
	nosetests

*Nose* is a unit testing software. It looks for files that start with *test_* (or *Test_*, or *test-*, or *Test-*). Inside these files it looks for test functions (that match the pattern above) and executes. If the test passes or fails depends on the result of the *assert* statement. *Nose* then prints a summary of the test results.


``Paste *rectangles.py* and * test_overlap.py* in the etherpad``

**Task. Write a test function for the test case from the previous exercise. (Some tests should fail, because there is a bug hidden in the code above)** [1]

1. How many tests should you write? A better question: How can you write as few tests as possible that still cover as many cases as possible? You want your tests to be distinct.
1. If you find a bug later, add it as a new test case.
1. Test the interface (how the function interacts with the outside, *given this input, I expect that output*), not the implementation (*how* the result is calculated).
1. Refactor: Write your code in such a way that it is easily testable. Ie write small functions that do one task, and one task only. (This also makes your code much more redable to your future self.)
1. Test early, and test often.

[1]. The Bug is in the *if* condition, *red_lo_y >= yellow_hi_x* should be *red_lo_y >= yellow_hi_y*. A typical copy&paste error.

## Test-driven development

Instead of writing the code first, and then test it, let's write the tests first! After all, we should know which functionality we want to add to our code before we start typing. This way, we also guaranteed that tests are *acutally* written.

A key idea is that *You ain't gonna need it* (YAGNI), ie only write just enough code to pass the tests. If you need more functionality, add more tests first. Soon, writing the code first and then test it will look backward to you.

``Example. You study the early phase of HIV infection. Typically, in the first few weeks the viral load increases exponentially to a peak and then decreases to a set point around which it then stays for several year. You want to extract the data points that correspond to viral load measurements from the exponential growth phase. Unfortunately, viral load measurements have a lower detection limit of 50 copies/ml, ie all measurements below this level are reported as 50 copies/ml.``

Hence, the function you want to write has to do the following:

1. Take a list of numbers, and return a (shorter) list of numbers.
1. Remove all leading values **50**.
1. Remove all values after the peak (remember, you want to study the growth part only).

Of course, we start writing the test cases first, one by one

	# file: test_extract.py
	from hiv import extract
	def test_extract_nothing_to_remove():
		vl = [100,200,500]
		obj=extract(vl)
		exp=vl
		assert obj==exp

To run the test, go to the shell and type

	nosetests

We see that the test fails because there is no file hiv.py with function extract (import error). *A success! We have a **red light**.*

Following YAGNI we only write just enough code to pass the test.

	# file: hiv.py
	# def extract(vl):
		return vl

This is enough to pass all of our tests. *Awesome! We have a **green light**.* As we see, this first version of *extract* will have to modified soon. But if all inputs this function will ever see are of the form of our first test, it would be sufficient to use this primitive version of *extract*.

To request more functionality, we write another test.

	# append to file: test_extract.py
	def test_extract_one_leading_50():
		vl = [50,100,200,500]
		obj=extract(vl)
		exp=[100,200,500]
		assert obj==exp

We hope to get a failing test, so we go to the shell

	nosetests

and indeed, the test fails. *Hooray! **Red light**.*

A failing test means we need to update the function.

	# file: hiv.py
	def extract(vl):
		if vl[0] != 50:
			return vl
		else:
			return vl[1:]


**Green Light**, nice. Of course, it is also possible that more than one test is negative. So, another test.

	# append to file: test_extract.py
	def test_extract_many_leading_50():
		vl = [50,50,50,50,100,200,500]
		obj=extract(vl)
		exp=[100,200,500]
		assert obj==exp

Again, this gives a **Red Light**, so we adjust our code in *hiv.py*. We see that we really want to keep removing leading entries of 50, and not stop at the first one. A natural solution is to use the *pop* method for a list, which removes the corresponding argument.

	# file: hiv.py
	def extract(vl):
		while vl[0] == 50:
			vl.pop(0)
		return vl

This gives a **Green Light**, and we are satisfied with how leading values of 50 are handled. Now, on to the second task: The function should also remove all values after the peak.

	# append to file: test_extract.py
	def test_extract_remove_one_after_peak():
		vl = [100,200,500,100]
		obj=extract(vl)
		exp=[100,200,500]
		assert obj==exp

	def test_extract_remove_many_after_peak():
		vl = [100,200,500,300,150,499,100]
		obj=extract(vl)
		exp=[100,200,500]
		assert obj==exp

Since both tests fail, we improve our function *extract*. We just want to return all values that are before the peak value:

	# file: hiv.py
	def extract(vl):
		while vl[0] == 50:
			vl.pop(0)
		peakIndex = vl.index(max(vl))
		return vl[:peakIndex+1]

So far, so good, **Green Light**. But, what do we expect if the peak value is repeated?

	# append to file: test_extract.py
	def test_extract_repeated_peaks():
		vl = [100,200,500,100,500,100,499,500,100]
		obj=extract(vl)
		exp=???
		assert obj==exp

This brings us back to one the strengths of testing in general, and test-driven development in particular: It lets us think about the Science, before we are busy thinking about the implementation. Since we want to study the growth phase, we want to remove every value after the first peak. Hence we choose *exp=[100,200,500]*. In fact, since the *index* method returns the first index, the test will pass without us having to modify our code. Now that we have this test, however, it documents the behavior we expect from the *extract* function.

Finally, let's write tests that combine the two steps:

	# append to file: test_extract.py
	def test_extract_leaving_50_repeated_peaks():
		vl = [50,50,50,100,200,500,130,499,500,300,100]
		obj=extract(vl)
		exp=[100,200,500]
		assert obj==exp

Good job, this test also passes! At this point we could be happy and done. However, we later realize that there may be more elegant solutions than testing for leading 50s in a *while* loop. We could use logical indexing instead. With the tests in place, we are confident to **refactor** our code, that is, improve the *implementation* (how the program does what it does), while leaving the *intreface* (what the program does) intact.

	# file hiv.py
	def extract(vl):
		#viral loads with undetectable after peak are not scientifically sound. Double check measurements.
		if vl.count(50) and len(vl)-1-vl[::-1].index(50) > vl.index(max(vl)):
			return []
		vl = [x for x in vl if x != 50]
		return vl[:vl.index(max(vl))+1]

The *if* condition first checks if undetectable values have been measured. If so, then the *last* undetectable should not be after the peak. Finally, for good measure, we might as well throw in a boundary case where all measurements were undetectable. The final version of test_extract.py is below.


**Final version of test_extract.py**
	from hiv import extract

	def test_extract_nothing_to_remove():
		vl=[100,200,500]
		obj=extract(vl)
		exp=vl
		assert obj==exp
	
	def test_extract_one_leading_50():
		vl = [50,100,200,500]
		obj=extract(vl)
		exp=[100,200,500]
		assert obj==exp
	
	def test_extract_many_leading_50():
		vl = [50,50,50,50,100,200,500]
		obj=extract(vl)
		exp=[100,200,500]
		assert obj==exp
	
	def test_extract_remove_one_after_peak():
		vl = [100,200,500,100]
		obj=extract(vl)
		exp=[100,200,500]
		assert obj==exp
	
	def test_extract_remove_many_after_peak():
		vl = [100,200,500,300,150,499,100]
		obj=extract(vl)
		exp=[100,200,500]
		assert obj==exp
	
	def test_extract_repeated_peaks():
		vl = [100,200,500,100,500,100,499,500,100]
		obj=extract(vl)
		exp=[100,200,500]
		assert obj==exp
	
	def test_extract_leaving_50_repeated_peaks():
		vl = [50,50,50,100,200,500,130,499,500,300,100]
		obj=extract(vl)
		exp=[100,200,500]
		assert obj==exp

	def test_extract_50_after_peak():
		vl = [50,50,100,200,500,100,50,100]
		obj=extract(vl)
		exp=[]
		assert obj==exp
	
	def test_extract_only_untedectable():
		vl = [50,50,50]
		obj=extract(vl)
		exp=[]
		assert obj==exp


## Not covered here

1. If read from file, don't rely on file being at a certain spot in your directory tree. Chances are that sooner or later it will be moved or lost. Instead, check out *StringIO*.
1. To avoid duplicate code, and to prevent the result from one test to influence the other, check out *setup*, *fixtures*, and *decorators*.
1. When working with floating points (non-integers), the *==* doesn't really make sense. In *nose.tools* there is special assertions for that instead, eg. *assert_almost_equal* with an error tolerance.
1. Of course, you can also test for exceptions, eg. you can assert if a certain type of error is thrown, given a certain input.
