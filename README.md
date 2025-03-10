# John O. Agumba-Capstone-Project
# <span style="color: orange;">Bellabeat Capstone using Fitbeat Data- Analysis using Python</span>

## <span style="color: blue;">Introduction</span>
### Company Background
Bellabeat, founded in 2013 by Urška Sršen and Sando Mur, is a high-tech company focused on health products for women. It is a successful small company, but they have the potential to become a larger player in the global <smart>(https://en.wikipedia.org/wiki/Smart_device) device market. <Click here>(https://bellabeat.com/) for more information about the company. Sršen, leveraging her artistic background, developed beautifully designed technology that tracks _activity, sleep, stress, and reproductive health_. This data-driven approach empowers women to understand their health and habits. By 2016, Bellabeat expanded globally, launching multiple products and opening offices worldwide. The company's products are available through online retailers and their e-commerce website (<Bellabeat Website>(https://bellabeat.com/)). Bellabeat combines traditional advertising methods, such as radio, billboards, print, and TV, with a strong focus on digital marketing. They invest in Google Search, maintain active social media presence on Facebook, Instagram, and Twitter, and run video ads on YouTube and display ads through Google Display Network to support key marketing campaigns.

### My Business Problem
As a data analyst, the business problem I needed to solve was to analyze Bellabeat's consumer data to uncover insights into how users are interacting with their smart devices. Sršen wanted me to focus on understanding the usage patterns related to _activity and sleep tracking_. By analyzing this data, I aimed to identify trends in device usage, including which features are used most often, the time of day or circumstances when the devices are most active, and how these behaviors vary across different customer demographics.

Additionally, I looked for any gaps in usage or underutilized features. From this analysis, I generated high-level recommendations that could inform Bellabeat's marketing strategy. Ultimately, the goal was to help Bellabeat drive growth by aligning their product offerings and marketing efforts more closely with consumer habit. To do this, I followed the six steps of the data analysis process: *ask, prepare, process, analyze, share, and act*, to break down how I analyzed the <FitBit fitness Tracker Data>(https://www.kaggle.com/datasets/arashnic/fitbit) in order to gain some insights that could be beneficial to Bellabeat.

## 1. Ask
### 1.1 Stakeholders
The key stakeholders in this project included the following:
1. Urška Sršen: Cofounder and Chief Creative Officer at Bellabeat.
2. Sando Mur: Cofounder and key member of the Bellabeat executive team.
3. Marketing analytics team at Bellabeat: A team of data analysts responsible for collecting, analyzing, and reporting data that helps guide  Bellabeat’s marketing strategy.
4. Customers: Everyone who purchases their product or use Bellabeat’s services.


### 1.2 Business Questions
My work was to analyze smart device usage data to gain insights into how consumers were using Bellabeat smart devices. I needed to understand broader trends that could be applied to Bellabeat’s own product offerings. After identifying these trends, I was to select one Bellabeat product and apply the insights to it for my presentation.

The analysis was guided by the following questions:

i.   What were the key trends in smart device usage?
ii.  How could these trends be applied to Bellabeat’s customer base?
iii. How could these trends influence Bellabeat’s marketing strategy?
iv.  The final deliverables for the report included:

A clear summary of the business task
i.   A description of all data sources used in the analysis
ii.  Documentation of any data cleaning or manipulation performed
iii. A summary of my analysis and findings
iv.  Supporting visualizations to illustrate key insights
v.   My top high-level content recommendations based on the analysis

I followed the Case Study Roadmap as a guide and completed the case study within a week.

## 2. Prepare

### 2.1 Data Source
The data used is a free to use <FitBit Fitness tracker dataset>(https://www.kaggle.com/datasets/arashnic/fitbit) made available through Mobius. It contains personal fitness tracker data from over thirty FitBit users who have given consent to use their data. There are 18 csv files in all, but from the datasets I found only a few datasets relevant for my analysis. I thus focused on dailyActivity_merged.csv, hourlyCalories_merged.csv, hourlySteps_merged.csv, daily_Calories_merged.csv, dailySteps_merged.csv, dailyIntensities_merged.csv and sleepDay_merged.csv datasets_.

### 2.2 Data Sorting
To quickly review the data, I opened each file in excel and observed that the data was structured in both wide and long formats. I also noticed that the dailyActivity_merged dataset included several metrics that could provide valuable insights, such as the total number of steps taken by Fitbit users, active minutes, and calories burned. These metrics could allow us to explore potential correlations, particularly between calories burned and steps taken. Additionally, the hourly calories and hourly steps datasets contained information on activity by hour, which would help provide insights into how calories and steps are distributed throughout the day.

Next, I organized the files by creating a separate folder on my Capstone Project folder, as I planned to use Python and Jupyter Notebook to process the data.

### 2.3 Data Credibility and Reliability
1. The credibility of Fitbit datasets: This depended on many factors, including data collection methods, device accuracy, and the consistency of the data over time. Here’s a breakdown of the factors that contribute to the data's credibility:

2. Data Collection: Fitbit devices collect data directly from users, capturing real-time activity metrics, such as steps, heart rate, calories burned, and sleep patterns. This makes the data reliable for tracking personal health metrics on a day-to-day basis, but the accuracy depends on users wearing the device consistently and correctly.

3. Device Accuracy: Fitbit devices use sensors such as accelerometers, heart rate monitors, and GPS for data collection. While Fitbit’s devices are generally accurate, some studies have shown that their step counters and calorie estimations can have slight discrepancies compared to medical-grade equipment.

4. Consistency: Fitbit datasets tend to be consistent for long-term usage, assuming users are regularly wearing their devices. However, variations in how often users sync their data, the type of activities they engage in, or how they use the device could introduce some inconsistencies.

5. Sampling Bias: Fitbit data is often self-reported through users who voluntarily choose to use the device, which means the data may not be representative of the general population. Users may also vary in how accurately they input information about their health habits.

6. Data Integrity: Fitbit datasets are typically well-maintained, with proper data formatting and storage practices. However, errors may still occur in syncing data or processing it into datasets, which should be handled during the analysis phase.

Overall, Fitbit datasets are generally credible for personal health insights and large-scale analysis, but potential issues related to device accuracy, consistency, and sampling bias should be considered when drawing conclusions from the data.

## 3. Process
The Fitbit data was processed to extract meaningful insights about users' activities, sleep patterns, and health metrics. The following steps were used to process the datasets that includes activity logs, step counts, calories burned, sleep data, and other variables.

Here’s a general outline of the steps involved in processing Fitbit data:
### a. Loading the Datasets
The first step is to load the Fitbit data from a CSV file or other data format (e.g., .xlsx, .json) using libraries such as pandas. The data could include activity and sleep data over several hours or days.
### b. Cleaning and Preprocessing the Datasets
Handling Missing or Inconsistent Data: Missing or corrupted data entries are identified and removed or filled. For example, if a column contains "NaN" or missing values, they can be dropped or filled using appropriate techniques.
Datetime Conversion: Many Fitbit datasets include date and time columns (e.g., ActivityDate, ActivityHour, SleepDay). These columns need to be converted to datetime objects for easy manipulation and analysis.
### c. Merging Datasets
Fitbit data is often recorded across different files, such as hourly steps, hourly calories, and sleep data. These datasets need to be merged based on common columns like Id (user ID) or ActivityHour (timestamp). Merging allows the datasets to be combined into one comprehensive dataset for further analysis.

## 4. Analyzing the Data
After cleaning and merging the data, it's time to perform data analysis to extract insights. Some common analyses on Fitbit data include:
Step counts: Summarizing total steps per day or over a specific time period.
Calories burned: Calculating the total calories burned based on activity levels.
Active minutes: Calculating time spent in different activity levels (e.g., sedentary, light active, very active).
Sleep patterns: Analyzing the amount of time spent in deep sleep, light sleep, or awake.
Active hours: Analyzing the hours of the day when users are most or least active.

## 5. Share
Visualizing the Data
Once the data is cleaned, merged, and analyzed, it can be visualized using matplotlib or seaborn to identify trends and insights. Visualizations like bar charts, line graphs, and scatter plots are commonly used to display the relationships between variables such as steps, calories, and active minutes.

## 6. Act
Finally, insights were drawn based on the analysis. Some possible insights could include: Active times of the day: Identifying the hours when users are most and least active, Sleep habits: Analyzing how sleep durations correlate with activity levels or calories burned.
User trends: Observing differences in activity across days of the week (e.g., more active on weekdays vs weekends).

Based on the processed Fitbit data, recommendations were made: These include: Increase Physical Activity: Since most users were sedentary, ways to increase activity throughout the day were recommended. Using active hours were recommended to push advertisements or notifications at optimal times to engage users when they are active.
