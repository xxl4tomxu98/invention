<!---
Questions? Comments?
1. Log an issue to this repo to alert us of a problem.
2. Suggest an edit yourself by forking this repo, making edits, and submitting a pull request with your changes back to our master branch.
3. Reach out to the Data team on Slack and share your thoughts!
--->

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Robust Regression

> Flex Lesson

---

## Materials We Provide
<!--- This section is a table of contents for the activity. The table structure breaks down repo resources into types, distinguishing between notebooks and supporting materials. Note that the table below demonstrates the total possible range of materials. Most lessons won't require all of these categories. Also note that every item in the repo should get its own line and link. --->

| Topic | Description | Link |
| --- | --- | --- |
| Lesson | Robust Regression Lesson | [Link](./robust-regression.ipynb)|
| Activity | Robust Regression Activity | [Link](./baltimore-salaries-lab.ipynb)|
| Data Set | Lemonade Data Used in Lesson | [Link](./data/lemonade-stand.csv)|
| Data Set | Baltimore City Employee Salaries Used in Activity | [Link](./data/Baltimore_City_Employee_Salaries_2011.csv)|


> **Data description**: `lemonade-stand.csv` is a data set of lemonade sales and their relationship to temperature and humidity. The Baltimore City Employee Salaries data is pretty self-explanatory.

> **Note:** This lesson involves some hands-on physical activities. You might want to check whether there is a large open
> space available. As an optional extension, we recommend bringing in a ball of string and a large number of numbered counters; this type of interactive visual activity can make for a more enjoyable experience (and a faster one, too).

---

## Learning Objectives
<!--- This section lists the lesson's learning objectives. For information on how to write clear learning objectives, review [this resource](http://ii.library.jhu.edu/2016/07/20/writing-effective-learning-objectives/). --->

- **Review** the limitations and shortcomings of OLS and the $R^2$ scoring function.
- **Define** when to use robust regression methods instead of OLS.
- **Demonstrate** how Theil-Sen, RANSAC, and Huber work and what they are optimizing for.
- **Explain** the advantages of using median absolute error as a scoring function.
- **Create** a scoring function that's appropriate for different business scenarios.

---

## Student Requirements
<!--- This section explains the relevant prerequisites — in other words, what students need to know to be able to benefit from and perform the tasks required in this activity/lab. List all of the relevant skills or prior learning objectives here. --->

**Before this activity, students should already be able to**:
- Split a data set into training and testing parts.
- Create a linear model using `sklearn.linear_model.LinearRegression`.
- Create a scatterplot using Matplotlib.
- Understand the concept of error in a prediction.

---

## Lesson Outline

<!--- This section outlines the lesson plan with relevant sections and subsections, providing both the total time required as well as suggestions for timing in each subsection. --->

> Total time: 80 min 

- **Introduction** (5 min)
- **Review of Ordinary Least Squares** (25 min)
    - Review (10 min)
	- Why We Like `$R^2$` (4 min)
	- Problems With `$R^2$` (5 min)
	- Alternatives (3 min)
- **Robust Regression** (35 min)
	- Theil-Sen (15 min including activity)
	- RANSAC (15 min including activity)
	- Huber (5 min)
- **Median Absolute Error** (5 min)
- **Scenario-Specific Scoring Functions** (5 min)
	- Lemonade Stand (5 min)
- **Review**
- **Break**
- **Activity** (90 min)
	- Section 1 (50 min)
   		- Read the Data Set
		- Preprocess the Data (Convert Strings to Numbers)
		- Perform EDA
		- Create Training and Testing Sets
		- Plot OLS
		- Plot Results From Linear vs. OLS
		- Calculate Metrics for Comparison
		- Repeat Analysis Using Alternate Methods
			- Theil-Sen
			- RANSAC
			- Huber
- Section 2 (40 min)
	- Create a Scoring Function
	- Score the Four Models
**Bonus**
	- Find the Optimal Coefficient
	- Improve the Model


## Activity Objectives
<!--- This section lists the learning objectives of the activity or lab.  --->

This lesson includes independent activities that allow students to apply the concepts learned. The requirements/steps for these activities are:

<!--- This section lists the exact requirements students have to perform in order to "complete" the activity.  --->
#### Requirements
1. Complete Section 1
   1. Read the Data Set
   1. Preprocess the Data (Convert Strings to Numbers)
   1. Perform EDA
   1. Create Training and Testing Sets
   1. Plot OLS
   1. Plot Results From Linear vs. OLS
   1. Calculate Metrics for Comparison
   1. Repeat Analysis Using Alternate Methods
      - Theil-Sen
      - RANSAC
      - Huber
1. Complete Section 2
   1. Create a Scoring Function
   1. Score the Four Models

**Bonus**
1. Find the Optimal Coefficient
1. Improve the Model

---

## Additional Resources
<!--- List of potential sources that may help or inform the students' ability to complete the tasks required. This might include reference sites, examples, or tutorials for "getting started." --->

For more information on this topic, check out the following resources:
- [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/)
- [The More Advanced Book: The Elements of Statistical Learning](http://web.stanford.edu/~hastie/ElemStatLearn/)
- [Spurious Correlations](http://www.tylervigen.com/spurious-correlations)
- Wikipedia pages on [ANOVA](https://en.wikipedia.org/wiki/Analysis_of_variance), [Welch's T-Test](https://en.wikipedia.org/wiki/Welch's_t-test), and the [Mann-Whitney Test](https://en.wikipedia.org/wiki/Mann%E2%80%93Whitney_U_test)
- [The RANSAC Song](http://danielwedge.com/ransac/)
