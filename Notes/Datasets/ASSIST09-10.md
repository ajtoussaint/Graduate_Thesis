## Description

Data was collected from 2004-2006 from two middle schools in Massachusetts. ASSISTMENTS included 493 main questions and an additional 1216 scaffolding questions. 912 8th grade students performance in the system was logged from September to May for each school year. Complete data from 417 students was obtained for the data set for the 2004-2005  school year and 616 students from the 2005-2006 school year.

According to [[Wang, Fei, et al. 2022]] the assist data logs are stable and viable for use with statistic models.

Feng, M., Heffernan, N.T., & Koedinger, K.R. (2009). Addressing the assessment challenge in an Intelligent Tutoring System that tutors as it assesses. _The Journal of User Modeling and User-Adapted Interaction, 19_, 243-266

## Columns
- order_id:  These id's are chronological, and refer to the id of the original problem log.
- assignment_id Two different assignments can have the same sequence id. Each assignment is specific to a single teacher/class.
- user_id: The ID of the student doing the problem.
- assistment_id: The ID of the ASSISTment. An ASSISTment consists of one or more problems.
- problem_id: The ID of the problem.
- original
    - 1 = Main problem
	- 0 = Scaffolding problem
- **correct**
    - 1 = Correct on first attempt
    - 0 = Incorrect on first attempt, or asked for help.
	-  [This column is often the target for prediction](http://www.google.com/url?q=http%3A%2F%2Fteacherwiki.assistment.org%2Findex.php%3Ftitle%3DThis_column_is_often_the_target_for_prediction%26action%3Dedit%26redlink%3D1&sa=D&sntz=1&usg=AOvVaw1oJvyU1sd3keiLrDk8NzEk)
- attempt_count: Number of student attempts on this problem.
- ms_first_response: The time in milliseconds for the student's first response.
- tutor_mode: tutor, test mode, pre-test, or post-test
- answer_type
    -  choose_1: Multiple choice (radio buttons)
	- algebra: Math evaluated string (text box)
	- fill_in: Simple string-compared answer (text box)
	- open_response: Records student answer, but their response is always marked correct
- sequence_id: The content id of the problem set. Different assignments that assign the same problem set will have the same sequence id.
- student_class_id: The class ID.
- position: Assignment position on the class assignments page.
- problem_set_type:
    -  Linear - Student completes all problems in a predetermined order.
	- Random - Student completes all problems, but each student is presented with the problems in a different random order.
	- Mastery - Random order, and student must "master" the problem set by getting a certain number of questions correct in a row before being able to continue.
- base_sequence_id: This is to account for if a sequence has been copied. This will point to the original copy, or be the same as sequence_id if it hasn't been copied.
- list_skill_ids: A semi-colon-delimited list of the IDs of the skills associated with the problem.
- list_skills: A semi-colon-delimited list of the skills associated with the problem.
- teacher_id: The ID of the teacher who assigned the problem.
- school_id: The ID of the school where the problem was assigned.
## Links
[assistments_2009_2010.zip - Google Drive](https://drive.google.com/file/d/0B2X0QD6q79ZJNEdiMHkyb0RNQlE/view?resourcekey=0-hZLp6qVFN8i6y0D3BbVuoQ)

https://sites.google.com/site/assistmentsdata/home/assistment-2009-2010-data/combined-dataset-2009-10

[ASSISTmentsData (google.com)](https://sites.google.com/site/assistmentsdata/datasets?authuser=0)