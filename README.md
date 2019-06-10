## Autograding ##

This repo contains the autograder code for xv6 projects.

The autograder infrastructure was given to us by a TA at UW-Madison where they also teach xv6.  We then modified it as needed and created our own tests to go along with our projects.
The fact that the infrastructure was created elsewhere has a few implications:  

* You may see references to unfamiliar things like "cs537" and "project4b" and so on.  As you can guess, these apply to the UW-Madison course, not the Northwestern course.  These names should either be ignored, deleted, or updated.
* The documentation (i.e. this README) is very sparse relative to the complexity of the repo.  Please update/add documentation as you figure things out.

### Run tests on a single submission ###

1. Navigate to the base directory of the xv6 code you want to test.
2. From that directory, execute the runtests executable in this directory.  Something like this:
`$ <path-to-autograder>/tests/runtests-proj3`
3. The individual tests are available in the **ctests/** folder. You can copy the file you want into your user program and run it locally as you wish.
The output from runtests will indicate which tests you have passed and which you failed (if any)

For more options available while testing, run '.../runtests -h'
		
No need to wait for student submissions to start playing with this.  You can and 
should do a test run of the autograder on your own xv6 code to assure yourself that things are working properly.

### Run tests on a bunch of submissions ###

1. Put autograding under your `~` folder to make its path to be like `~/autograding`.
2. Put all submission repos in a root folder. For example, create a folder `~/allrepos` and put `proj1_kaiyuhou` and `proj1_kaiyuhou2` directly under `~/allrepos`.
3. Naviagete to this root folder.
4. execute the command. Proj1: `~/autograding/tests/batch_runtests`, Proj2: `~/autograding/tests/batch_runtests2`, Proj3: `~/autograding/tests/batch_runtests3`, Proj4: `~/autograding/tests/batch_runtests4`.

The grading logs will be stored on the root directory of every submission as file like `runtests_regrade1.log`.

### Directories and Files ###
* **tests/** Contains more important files for running tests.  See the README within the directory for more info.
* **tools/** Additional tools.  See the README within the directory for more info.
* **.gitignore** files and extensions to ignore
* **README** this thing you are reading
