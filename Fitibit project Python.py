# %% [markdown]
# # <span style="color: orange;">Bellabeat Capstone using Fitbeat Data- Analysis using Python</span>
# 
# ## <span style="color: blue;">Introduction</span>
# ### Company Background
# Bellabeat, founded in 2013 by Urška Sršen and Sando Mur, is a high-tech company focused on health products for women. It is a successful small company, but they have the potential to become a larger player in the global <smart>(https://en.wikipedia.org/wiki/Smart_device) device market. <Click here>(https://bellabeat.com/) for more information about the company. Sršen, leveraging her artistic background, developed beautifully designed technology that tracks _activity, sleep, stress, and reproductive health_. This data-driven approach empowers women to understand their health and habits. By 2016, Bellabeat expanded globally, launching multiple products and opening offices worldwide. The company's products are available through online retailers and their e-commerce website (<Bellabeat Website>(https://bellabeat.com/)). Bellabeat combines traditional advertising methods, such as radio, billboards, print, and TV, with a strong focus on digital marketing. They invest in Google Search, maintain active social media presence on Facebook, Instagram, and Twitter, and run video ads on YouTube and display ads through Google Display Network to support key marketing campaigns.
# 
# ### My Business Problem
# As a data analyst, the business problem I needed to solve was to analyze Bellabeat's consumer data to uncover insights into how users are interacting with their smart devices. Sršen wanted me to focus on understanding the usage patterns related to _activity and sleep tracking_. By analyzing this data, I aimed to identify trends in device usage, including which features are used most often, the time of day or circumstances when the devices are most active, and how these behaviors vary across different customer demographics.
# 
# Additionally, I looked for any gaps in usage or underutilized features. From this analysis, I generated high-level recommendations that could inform Bellabeat's marketing strategy. Ultimately, the goal was to help Bellabeat drive growth by aligning their product offerings and marketing efforts more closely with consumer habit. To do this, I followed the six steps of the data analysis process: *ask, prepare, process, analyze, share, and act*, to break down how I analyzed the <FitBit fitness Tracker Data>(https://www.kaggle.com/datasets/arashnic/fitbit) in order to gain some insights that could be beneficial to Bellabeat.
# 
# ## <span style="color: blue;">1. Ask</span>
# ### 1.1 Stakeholders
# The key stakeholders in this project included the following:
# 1. Urška Sršen: Cofounder and Chief Creative Officer at Bellabeat.
# 2. Sando Mur: Cofounder and key member of the Bellabeat executive team.
# 3. Marketing analytics team at Bellabeat: A team of data analysts responsible for collecting, analyzing, and reporting data that helps guide  Bellabeat’s marketing strategy.
# 4. Customers: Everyone who purchases their product or use Bellabeat’s services.
# 
# 
# ### 1.2 Business Questions
# My work was to analyze smart device usage data to gain insights into how consumers were using Bellabeat smart devices. I needed to understand broader trends that could be applied to Bellabeat’s own product offerings. After identifying these trends, I was to select one Bellabeat product and apply the insights to it for my presentation.
# 
# The analysis was guided by the following questions:
# 
# i.   What were the key trends in smart device usage?
# ii.  How could these trends be applied to Bellabeat’s customer base?
# iii. How could these trends influence Bellabeat’s marketing strategy?
# iv.  The final deliverables for the report included:
# 
# A clear summary of the business task
# i.   A description of all data sources used in the analysis
# ii.  Documentation of any data cleaning or manipulation performed
# iii. A summary of my analysis and findings
# iv.  Supporting visualizations to illustrate key insights
# v.   My top high-level content recommendations based on the analysis
# 
# I followed the Case Study Roadmap as a guide and completed the case study within a week.
# 
# ## <span style="color: blue;">2. Ask</span>
# 
# ### 2.1 Data Source
# The data used is a free to use <FitBit Fitness tracker dataset>(https://www.kaggle.com/datasets/arashnic/fitbit) made available through Mobius. It contains personal fitness tracker data from over thirty FitBit users who have given consent to use their data. There are 18 csv files in all, but from the datasets I found only a few datasets relevant for my analysis. I thus focused on dailyActivity_merged.csv, hourlyCalories_merged.csv, hourlySteps_merged.csv, daily_Calories_merged.csv, dailySteps_merged.csv, dailyIntensities_merged.csv and sleepDay_merged.csv datasets_.
# 
# ### 2.2 Data Sorting
# To quickly review the data, I opened each file in excel and observed that the data was structured in both wide and long formats. I also noticed that the dailyActivity_merged dataset included several metrics that could provide valuable insights, such as the total number of steps taken by Fitbit users, active minutes, and calories burned. These metrics could allow us to explore potential correlations, particularly between calories burned and steps taken. Additionally, the hourly calories and hourly steps datasets contained information on activity by hour, which would help provide insights into how calories and steps are distributed throughout the day.
# 
# Next, I organized the files by creating a separate folder on my Capstone Project folder, as I planned to use Python and Jupyter Notebook to process the data.
# 
# ### 2.3 Data Credibility and Reliability
# 1. The credibility of Fitbit datasets: This depended on many factors, including data collection methods, device accuracy, and the consistency of the data over time. Here’s a breakdown of the factors that contribute to the data's credibility:
# 
# 2. Data Collection: Fitbit devices collect data directly from users, capturing real-time activity metrics, such as steps, heart rate, calories burned, and sleep patterns. This makes the data reliable for tracking personal health metrics on a day-to-day basis, but the accuracy depends on users wearing the device consistently and correctly.
# 
# 3. Device Accuracy: Fitbit devices use sensors such as accelerometers, heart rate monitors, and GPS for data collection. While Fitbit’s devices are generally accurate, some studies have shown that their step counters and calorie estimations can have slight discrepancies compared to medical-grade equipment.
# 
# 4. Consistency: Fitbit datasets tend to be consistent for long-term usage, assuming users are regularly wearing their devices. However, variations in how often users sync their data, the type of activities they engage in, or how they use the device could introduce some inconsistencies.
# 
# 5. Sampling Bias: Fitbit data is often self-reported through users who voluntarily choose to use the device, which means the data may not be representative of the general population. Users may also vary in how accurately they input information about their health habits.
# 
# 6. Data Integrity: Fitbit datasets are typically well-maintained, with proper data formatting and storage practices. However, errors may still occur in syncing data or processing it into datasets, which should be handled during the analysis phase.
# 
# Overall, Fitbit datasets are generally credible for personal health insights and large-scale analysis, but potential issues related to device accuracy, consistency, and sampling bias should be considered when drawing conclusions from the data.

# %% [markdown]
# ## <span style="color: blue;">3. Process</span>
# 
# ### 3.1 Loading Libraries and Datasets
# #### 3.1.1 Loading Libraries
# The following libraries were loaded.
# 

# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

# %% [markdown]
# #### 3.1.2 Loading Datasets
# 
# Now, we loaded all the fitbit datasets. However, only some will be explored for analysis and insights

# %%
daily_activity = pd.read_csv('dailyActivity_merged.csv')
hourly_steps = pd.read_csv('hourlySteps_merged.csv')
hourly_calories = pd.read_csv('hourlyCalories_merged.csv')
sleepday = pd.read_csv('sleepDay_merged.csv')
daily_calories = pd.read_csv('dailyCalories_merged.csv')
daily_intensity = pd.read_csv('dailyIntensities_merged.csv')
weight_log = pd.read_csv('weightLogInfo_merged.csv')
daily_steps = pd.read_csv('dailySteps_merged.csv')
heartrate_secs = pd.read_csv("heartrate_seconds_merged.csv")
hourly_intensities = pd.read_csv('hourlyIntensities_merged.csv')
minuteCaloriesNarrow = pd.read_csv('minuteCaloriesNarrow_merged.csv')
minuteCaloriesWide = pd.read_csv('minuteCaloriesWide_merged.csv')
minuteIntensitiesNarrow = pd.read_csv('minuteIntensitiesNarrow_merged.csv')
minuteIntensitiesWide = pd.read_csv('minuteIntensitiesWide_merged.csv')
minuteMETsNarrow = pd.read_csv('minuteMETsNarrow_merged.csv')
minuteSleep = pd.read_csv('minuteSleep_merged.csv')
minuteStepsNarrow = pd.read_csv('minuteStepsNarrow_merged.csv')
minuteStepsWide = pd.read_csv('minuteStepsWide_merged.csv')


# %% [markdown]
# ### 3.2 Data Exploration
# I took initial steps to investigate a datasets to understand their main characteristics. This I did through visual and statistical techniques. 

# %% [markdown]
# #### 3.2.1 Dataset Preview
# I performed preview of each dataset as seen below.

# %% [markdown]
# #### daily_activity

# %%
daily_activity.head()


# %% [markdown]
# ####  hourly_steps

# %%
hourly_steps.head()


# %% [markdown]
# #### hourly_calories

# %%
hourly_calories.head()


# %% [markdown]
# #### sleepday

# %%
sleepday.head()


# %% [markdown]
# #### daily_calories

# %%
daily_calories.head()


# %% [markdown]
# #### daily_intensity

# %%
daily_intensity.head()


# %% [markdown]
# #### weight_log

# %%
weight_log.head()


# %% [markdown]
# #### daily_steps

# %%
daily_steps.head()


# %% [markdown]
# #### heartrate_secs

# %%
heartrate_secs.head()

# %% [markdown]
# #### hourly_intensities

# %%
hourly_intensities.head()

# %% [markdown]
# #### minuteCaloriesNarrow

# %%
minuteCaloriesNarrow.head()

# %% [markdown]
# #### minuteCaloriesWide

# %%
minuteCaloriesWide.head()

# %% [markdown]
# #### minuteIntensitiesNarrow

# %%
minuteIntensitiesNarrow.head()

# %% [markdown]
# #### minuteIntensitiesWide

# %%
minuteIntensitiesWide.head()

# %% [markdown]
# #### minuteMETsNarrow

# %%
minuteMETsNarrow.head()

# %% [markdown]
# #### minuteSleep

# %%
minuteSleep.head()

# %% [markdown]
# #### minuteStepsNarrow

# %%
minuteStepsNarrow.head()

# %% [markdown]
# #### minuteStepsWide

# %%
minuteStepsWide.head()

# %% [markdown]
# #### 3.2.2 Calculation of the size (n) of the datasets
# We next checked on the sizes of each dataset.
# 

# %%
import pandas as pd

# Define file names and paths
file_paths = {
    "Daily Activity": 'dailyActivity_merged.csv',
    "Hourly Steps": 'hourlySteps_merged.csv',
    "Hourly Calories": 'hourlyCalories_merged.csv',
    "Sleepday": 'sleepDay_merged.csv',
    "Daily Calories": 'dailyCalories_merged.csv',
    "Daily Intensity": 'dailyIntensities_merged.csv',
    "Weight Log": 'weightLogInfo_merged.csv',
    "Daily Steps": 'dailySteps_merged.csv',
    "Heart Rate": 'heartrate_seconds_merged.csv',
    "Hourly Intensities": 'hourlyIntensities_merged.csv',
    "Minute Calories Narrow": 'minuteCaloriesNarrow_merged.csv',
    "Minute Calories Wide": 'minuteCaloriesWide_merged.csv',
    "Minute Intensities Narrow": 'minuteIntensitiesNarrow_merged.csv',
    "Minute Intensities Wide": 'minuteIntensitiesWide_merged.csv',
    "Minute METs Narrow": 'minuteMETsNarrow_merged.csv',
    "Minute Sleep": 'minuteSleep_merged.csv',
    "Minute Steps Narrow": 'minuteStepsNarrow_merged.csv',
    "Minute Steps Wide": 'minuteStepsWide_merged.csv'
}

# Load data and calculate sample sizes
for name, path in file_paths.items():
    try:
        df = pd.read_csv(path)
        n = df['Id'].nunique()  # Calculate unique participants (assuming 'Id' is the participant identifier)
        print(f"{name} Shape: {df.shape} | Sample Size (n) = {n}")
    except Exception as e:
        print(f"Error loading {name}: {e}")

# %% [markdown]
# ***Observation:***
# Of all the datasets we inspected by calculating the sample sizes (n), heartrate_secs, weight_logged and sleepday fell short of our n>=30 rule. heartrate_secs has sample size n=14, and weight_logged only has n=8, hence we decided to drop both of them. sleepday and minuteSleep both have n=24, which are much smaller than 30. However, we decided to keep them, just to see if they can unravel any meaningful insight.
# 
# daily_calories, daily_intensity, and daily_steps all have exactly the same data that was found in the daily_activity dataset. TotalDistance and TrackerDistance in daily_activity dataset were found to be similar. StepTotal in daily_steps was similar to TotalSteps in daily_activity datasets and thus, discarded. Leaving us with daily_activity, hourly_steps, hourly_calories, and sleepday datasets.
# 
# From the shape, we observed that hourly_steps and hourly_calories have similar structures: (22099, 3). Hence, we could decide to merge them for further analysis.
# 
# As for the data types, "ActivityDate” in daily_activity, “ActivityHour” in hourly_steps, “ActivityHour” in hourly_calories, and “SleepDay” in sleepday are objects instead of datetime data type. We’d convert them to datetime data type for easy processing.
# 
# We also observed that there were NO missing values and duplicates in all datasets.

# %% [markdown]
# #### 3.2.3 Drop Datasets with size n<20
# Based statistical considerations and the reliability of analysis, datasets with a sample size smaller than 30 were dropped.However, we kept minuteSleep_merged.csv with m=24 hoping to get some insights from it.

# %%
import pandas as pd

# Define file names and paths
file_paths = {
    "Daily Activity": 'dailyActivity_merged.csv',
    "Hourly Steps": 'hourlySteps_merged.csv',
    "Hourly Calories": 'hourlyCalories_merged.csv',
    "Sleepday": 'sleepDay_merged.csv',
    "Daily Calories": 'dailyCalories_merged.csv',
    "Daily Intensity": 'dailyIntensities_merged.csv',
    "Weight Log": 'weightLogInfo_merged.csv',
    "Daily Steps": 'dailySteps_merged.csv',
    "Heart Rate": 'heartrate_seconds_merged.csv',
    "Hourly Intensities": 'hourlyIntensities_merged.csv',
    "Minute Calories Narrow": 'minuteCaloriesNarrow_merged.csv',
    "Minute Calories Wide": 'minuteCaloriesWide_merged.csv',
    "Minute Intensities Narrow": 'minuteIntensitiesNarrow_merged.csv',
    "Minute Intensities Wide": 'minuteIntensitiesWide_merged.csv',
    "Minute METs Narrow": 'minuteMETsNarrow_merged.csv',
    "Minute Sleep": 'minuteSleep_merged.csv',
    "Minute Steps Narrow": 'minuteStepsNarrow_merged.csv',
    "Minute Steps Wide": 'minuteStepsWide_merged.csv'
}

# Load data, calculate sample sizes, and drop datasets with n < 20
valid_datasets = {}

for name, path in file_paths.items():
    try:
        df = pd.read_csv(path)
        n = df['Id'].nunique()  # Calculate unique participants (assuming 'Id' is the participant identifier)
        
        if n >= 20:
            valid_datasets[name] = df
            print(f"Keeping {name} | Shape: {df.shape} | Sample Size (n) = {n}")
        else:
            print(f"Dropping {name} | Shape: {df.shape} | Sample Size (n) = {n}")
    
    except Exception as e:
        print(f"Error loading {name}: {e}")

# %% [markdown]
# #### 3.2.4 Shapes of the Datasheets
# We sought to find the shapes of the remaining datasets
# 

# %%
# Define file names and load data
import pandas as pd
hourly_calories = pd.read_csv('hourlyCalories_merged.csv')
hourly_steps = pd.read_csv('hourlySteps_merged.csv')
hourly_intensities = pd.read_csv('hourlyIntensities_merged.csv')
daily_activity = pd.read_csv('dailyActivity_merged.csv')
daily_steps = pd.read_csv('dailySteps_merged.csv')
daily_calories = pd.read_csv('dailyCalories_merged.csv')
daily_intensity = pd.read_csv('dailyIntensities_merged.csv')
sleepday = pd.read_csv('sleepDay_merged.csv')


# Print column names for each DataFrame
print("Hourly Calories Columns:", hourly_calories.columns)
print("Hourly Steps Columns:", hourly_steps.columns)
print("Hourly Intensities Columns:", hourly_intensities.columns)
print("Daily Activity Shape:", daily_activity.shape)
print("Daily Steps Shape:", daily_steps.shape)
print("Daily Calories Shape:", daily_calories.shape)
print("Daily Intensity Shape:", daily_intensity.shape)
print("Sleepday Shape:", sleepday.shape)


# %% [markdown]
# #### 3.2.5 Checking for the Missing Values

# %%
# Define file names and load data
import pandas as pd

hourly_calories = pd.read_csv('hourlyCalories_merged.csv')
hourly_steps = pd.read_csv('hourlySteps_merged.csv')
hourly_intensities = pd.read_csv('hourlyIntensities_merged.csv')
daily_activity = pd.read_csv('dailyActivity_merged.csv')
daily_steps = pd.read_csv('dailySteps_merged.csv')
daily_calories = pd.read_csv('dailyCalories_merged.csv')
daily_intensity = pd.read_csv('dailyIntensities_merged.csv')
sleepday = pd.read_csv('sleepDay_merged.csv')

print("Number of missing values in the Hourly Calories Dataset is", hourly_calories.isnull().values.sum())
print("Number of missing values in the Hourly Steps Dataset is", hourly_steps.isnull().values.sum())
print("Number of missing values in the Hourly Intensities Dataset is", hourly_intensities.isnull().values.sum())
print("Number of missing values in the Daily Activity Dataset is",daily_activity.isnull().values.sum())
print("Number of missing values in the Daily Steps Dataset is",daily_steps.isnull().values.sum())
print("Number of missing values in the Daily Calories Dataset is",daily_calories.isnull().values.sum())
print("Number of missing values in the Daily Intensity Dataset is",daily_intensity.isnull().values.sum())
print("Number of missing values in the SleepDay Dataset is",sleepday.isnull().values.sum())



# %% [markdown]
# ### Observation:
# There were no missing values in all the datasets

# %% [markdown]
# #### 3.2.6 Checking for Duplicates
# We then checked on the datasets with duplicates.

# %%
import pandas as pd

# Load the data files
hourly_calories = pd.read_csv('hourlyCalories_merged.csv')
hourly_steps = pd.read_csv('hourlySteps_merged.csv')
hourly_intensities = pd.read_csv('hourlyIntensities_merged.csv')
daily_activity = pd.read_csv('dailyActivity_merged.csv')
daily_steps = pd.read_csv('dailySteps_merged.csv')
daily_calories = pd.read_csv('dailyCalories_merged.csv')
daily_intensity = pd.read_csv('dailyIntensities_merged.csv')

# Count duplicate rows
print("Number of Duplicate Rows in Hourly Calories Dataset:", hourly_calories.duplicated().sum())
print("Number of Duplicate Rows in Hourly Steps Dataset:", hourly_steps.duplicated().sum())
print("Number of Duplicate Rows in Hourly Intensities Dataset:", hourly_intensities.duplicated().sum())
print("Number of Duplicate Rows in Daily Activity Dataset:", daily_activity.duplicated().sum())
print("Number of Duplicate Rows in Daily Steps Dataset:", daily_steps.duplicated().sum())
print("Number of Duplicate Rows in Hourly Calories Dataset:", daily_calories.duplicated().sum())
print("Number of Duplicate Rows in Daily Intensity Dataset:", daily_intensity.duplicated().sum())
print("Number of Duplicate Rows in Sleepday Dataset:", sleepday.duplicated().sum())



# %% [markdown]
# Only the sleepDay_merged dataset had duplicated rows (3). We sought to identify the specific rows.

# %% [markdown]
# #### Showing the Duplicates in sleepDay_merged dataset

# %%
import pandas as pd

# Load the data files
sleepday = pd.read_csv('sleepDay_merged.csv')

# Find and display duplicate rows

print("\nDuplicate Rows in Sleepday Dataset:")
print(sleepday[sleepday.duplicated()])


# %% [markdown]
# #### Keeping only one of the Duplicated Rows in sleepDay_merged dataset
# The duplicated rows were dropped leaving only one row.

# %%
import pandas as pd

# Load the data files
sleepday = pd.read_csv('sleepDay_merged.csv')

# Drop duplicate rows based on all columns and reset the index
sleepday_clean = sleepday.drop_duplicates(keep='first').reset_index(drop=True)

# Print confirmation
print("Duplicate rows dropped. Cleaned datasets are ready!")
print(f"Sleepday: {sleepday_clean.shape[0]} rows")


# %% [markdown]
# #### 3.2.7 Checking the Columns of the Datasets

# %%
import pandas as pd

# Define file names and load data
hourly_calories = pd.read_csv('hourlyCalories_merged.csv')
hourly_steps = pd.read_csv('hourlySteps_merged.csv')
hourly_intensities = pd.read_csv('hourlyIntensities_merged.csv')
daily_activity = pd.read_csv('dailyActivity_merged.csv')
daily_steps = pd.read_csv('dailySteps_merged.csv')
daily_calories = pd.read_csv('dailyCalories_merged.csv')
daily_intensity = pd.read_csv('dailyIntensities_merged.csv')

# Print column names for each DataFrame
print("Hourly Calories Columns:", hourly_calories.columns.tolist())
print("Hourly Steps Columns:", hourly_steps.columns.tolist())
print("Hourly Intensities Columns:", hourly_intensities.columns.tolist())
print("Daily Activity Columns:", daily_activity.columns.tolist())
print("Daily Steps Columns:", daily_steps.columns.tolist())
print("Daily Calories Columns:", daily_calories.columns.tolist())
print("Daily Intensity Columns:", daily_intensity.columns.tolist())
print("Sleepday Columns:", sleepday_clean.columns.tolist())


# %% [markdown]
# ##### Observation: 
# 1. The ActivityDay columns in daily_steps_merged and daily_calories_merged are the same as the ActivityDate columns in daily_activity_merged dataset. Further, the Id, StepTotal column in daily_steps_merged dataset and Calories in daily_calories_merged datasets are found in daily_activity_datasets and thus are dropped.
# 2. The ActivityDay columns in houry_steps_merged and hourly_calories_merged were found to be the same as the ActivityDate columns in daily_activity_merged dataset. Further, the Id, StepTotal column in hourly_steps_merged dataset and Calories in hourly_calories_merged datasets awere found in daily_activity_datasets and thus are dropped.

# %% [markdown]
# #### 3.2.8 Final Datasets for Analysis
# Only 5 relevant datasets remained for analysis. These were daily_activity dataset, the daily_intensity dataset and the sleepday_clean dataset.

# %% [markdown]
# ##### 3.2.8.1 hourly_calories dataset

# %%

import pandas as pd

# Define file names and load data
hourly_calories = pd.read_csv('hourlyCalories_merged.csv')
print(hourly_calories.head())


# %% [markdown]
# ##### 3.2.8.2 daily_steps dataset

# %%
import pandas as pd

# Define file names and load data
hourly_steps = pd.read_csv('hourlySteps_merged.csv')
print(hourly_steps.head())


# %% [markdown]
# ##### 3.2.8.3 daily_activity dataset

# %%
import pandas as pd

# Define file names and load data
daily_activity = pd.read_csv('dailyActivity_merged.csv')

print(daily_activity.head)


# %% [markdown]
# ##### 3.2.8.4 daily_intensity dataset

# %%
import pandas as pd

# Define file names and load data
daily_intensity= pd.read_csv('dailyIntensities_merged.csv')
print(daily_intensity.head())

# %% [markdown]
# daily_intensity dataframe is brouped by ActivityDate and summed up in 8 columns

# %%
import pandas as pd

# Load the dataset
daily_intensity = pd.read_csv('dailyIntensities_merged.csv')

# Convert ActivityDay to date only (if needed)
daily_intensity['ActivityDay'] = pd.to_datetime(daily_intensity['ActivityDay']).dt.date

# Group by ActivityDay and sum the specified columns
daily_intensity = daily_intensity.groupby(['ActivityDay'], as_index=False).agg({
    'SedentaryMinutes': 'sum',
    'LightlyActiveMinutes': 'sum',	
    'FairlyActiveMinutes': 'sum',
    'VeryActiveMinutes': 'sum',
    'VeryActiveDistance': 'sum',
    'ModeratelyActiveDistance': 'sum',
    'LightActiveDistance': 'sum',
    'SedentaryActiveDistance': 'sum',
})

# Print the first few rows
print(daily_intensity.head(31))


# %% [markdown]
# ##### 3.2.8.5 sleepday_clean dataset
# We grouped the sleep_day dataframe by SleepDay colum and summed for the specified columns
# 

# %%

# Convert SleepDay to date only (remove time information) and drop the Id column
sleepday_clean['SleepDay'] = pd.to_datetime(sleepday_clean['SleepDay']).dt.date

# Group by SleepDay and sum the specified columns

sleepday_clean = sleepday_clean.groupby('SleepDay').agg({
    'TotalSleepRecords': 'sum',
    'TotalMinutesAsleep': 'sum',
    'TotalTimeInBed': 'sum',
}).reset_index()

# Show the first few rows
pd.set_option('display.max_columns', None)
print(sleepday_clean.head(39))


# %% [markdown]
# ### 3.3 Data Transformation
# #### 3.3.1 Renaming of the ActivityDay and sleepDay columns
# The  “ActivityDay” column in daily_intensity-merged dataset, and “SleepDay” column in sleepday_merged datasets are now renamed to match the "ActivityDate” column in daily_activity dataset

# %%
# Rename columns to match 'ActivityDate' in daily_activity dataset
daily_intensity.rename(columns={'ActivityDay': 'ActivityDate'}, inplace=True)
sleepday_clean.rename(columns={'SleepDay': 'ActivityDate'}, inplace=True)

# Print the first few rows to verify
print(daily_intensity.head())
print(sleepday_clean.head(31))


# %% [markdown]
# 

# %% [markdown]
# #### 3.3.2 Merge daily_intensity with sleepday_clean datasets
# 
# ##### Observation 
# The datasets share Id and ActivityDate in common. Hence, we merge them on Id and ActivityDate

# %%
# Merge the datasets on ActivityDate
merged_data1 = pd.merge(daily_intensity, sleepday_clean, on=['ActivityDate'], how='inner')

# Check the first few rows of the merged dataset
print(merged_data1.head(31))




# %% [markdown]
# 

# %% [markdown]
# We can as well achieve the same result using the code below.

# %%
# Merge the datasets on ActivityDate
merged_data1 = pd.merge(daily_intensity, sleepday_clean, on=['ActivityDate'], how='inner')

# Group by ActivityDate, then sum the specified columns
merged_data1 = merged_data1.groupby(['ActivityDate'], as_index=False).agg({
    'TotalSleepRecords': 'sum',
    'TotalMinutesAsleep': 'sum',
    'TotalTimeInBed': 'sum',
    'VeryActiveDistance': 'sum',
    'ModeratelyActiveDistance': 'sum',
    'LightActiveDistance': 'sum',
    'SedentaryActiveDistance': 'sum',
    'VeryActiveMinutes': 'sum',
    'FairlyActiveMinutes': 'sum',
    'LightlyActiveMinutes': 'sum',
    'SedentaryMinutes': 'sum',
})

# Show the grouped result
pd.set_option('display.max_columns', None)  # Ensure all columns are displayed
print(merged_data1.head(32))

# %% [markdown]
# #### 3.3.3. daily_activity dataset
# We sought to manupulate the dataset. We grouped it by ActivityDate column, then summed up the specified columns.

# %%

import pandas as pd

# Group by ActivityDate and ActivityDate, then sum the specified columns
daily_activity1 = daily_activity.groupby(['ActivityDate'], as_index=False).agg({
    'TotalSteps': 'sum',
    'TotalDistance': 'sum',
    'TrackerDistance': 'sum',
    'LoggedActivitiesDistance': 'sum',
    'VeryActiveDistance': 'sum',
    'ModeratelyActiveDistance': 'sum',
    'LightActiveDistance': 'sum',
    'SedentaryActiveDistance': 'sum',
    'VeryActiveMinutes': 'sum',
    'FairlyActiveMinutes': 'sum',
    'LightlyActiveMinutes': 'sum',
    'SedentaryMinutes': 'sum',
    'Calories': 'sum'
})

# Show the grouped result
pd.set_option('display.max_columns', None)  # Ensure all columns are displayed
print(daily_activity1)



# %% [markdown]
# #### 3.3.4 Merging daily_activity1 dataset with merged-data1
# Seeing that the two datasets were in the same shape and format, we now merged them using common columns.

# %%

# Convert ActivityDate to date format in both datasets
merged_data1['ActivityDate'] = pd.to_datetime(merged_data1['ActivityDate']).dt.date
daily_activity1['ActivityDate'] = pd.to_datetime(daily_activity1['ActivityDate']).dt.date

Final_Merged_dataframe1 = pd.merge(
    merged_data1, 
    daily_activity1,
    on=['ActivityDate', 'VeryActiveDistance', 'ModeratelyActiveDistance', 'LightActiveDistance', 
        'SedentaryActiveDistance', 'VeryActiveMinutes', 'FairlyActiveMinutes', 
        'LightlyActiveMinutes', 'SedentaryMinutes'], 
    how='inner'
)

Final_Merged_dataframe1.head(31)


# %% [markdown]
# #### 3.3.5 Create WeekDay Column
# 
# Drom the merged dataset, we now created a 'WeekDay' column

# %%
# Make sure the 'ActivityDate' column is in datetime format
Final_Merged_dataframe1['ActivityDate'] = pd.to_datetime(Final_Merged_dataframe1['ActivityDate'])
# Extract the weekday names from the date-time columns
Final_Merged_dataframe1["WeekDay"] = Final_Merged_dataframe1["ActivityDate"].dt.day_name()
Final_Merged_dataframe = Final_Merged_dataframe1

# Print the first few rows of the dataset to verify the changes
print("\nDaily Activity Clean:")
print(Final_Merged_dataframe.head())

# %%
# Make sure the 'ActivityDate' column is in datetime format
Final_Merged_dataframe['ActivityDate'] = pd.to_datetime(Final_Merged_dataframe['ActivityDate'])
# Extract the weekday names from the date-time columns
Final_Merged_dataframe["WeekDay"] = Final_Merged_dataframe["ActivityDate"].dt.day_name()

# Print the first few rows of the dataset to verify the changes
print("\nDaily Activity Clean:")
print(Final_Merged_dataframe.head())

# %% [markdown]
# #### 3.3.6 Final_Merged_dataframe

# %% [markdown]
# ##### 3.3.6.1 Shape

# %%
print(Final_Merged_dataframe.shape)

# %% [markdown]
# #### 3.3.6.2 Unique Dates & Missing values

# %%
print("Final_Merged_dataframe Dataframe has",Final_Merged_dataframe.ActivityDate.nunique(), "Unique Dates")
print("Merged_data3 DataFrame has",Final_Merged_dataframe.isnull().values.sum(), "missing values")

# %% [markdown]
# Observation-No missing values and 31 unique dates

# %%
Final_Merged_dataframe.head()

# %% [markdown]
# #### 3.3.7 Changes to Final_Merged dataframe
# Some changes to the Final_Merged dataframe1 was done for further analyses. Specifically, we created three additional columns (TotalActiveMinutes, TotalMinutes, and TotalActiveHours)

# %%
# Create new columns with values
Final_Merged_dataframe["TotalActiveMinutes"] = None
Final_Merged_dataframe["TotalMinutes"] = None
Final_Merged_dataframe["TotalActiveHours"] = None

# Calculate new columns
Final_Merged_dataframe["TotalActiveMinutes"] = Final_Merged_dataframe["VeryActiveMinutes"] + Final_Merged_dataframe["FairlyActiveMinutes"] + Final_Merged_dataframe["LightlyActiveMinutes"]
Final_Merged_dataframe["TotalMinutes"] = Final_Merged_dataframe["TotalActiveMinutes"] + Final_Merged_dataframe["SedentaryMinutes"]
Final_Merged_dataframe["TotalActiveHours"] = round(Final_Merged_dataframe["TotalActiveMinutes"] / 60)

# View the changes
Final_Merged_dataframe.head(31)


# %% [markdown]
# The columns were inserted and filled with calculated values.

# %% [markdown]
# ## <span style="color: blue;">4. Analyze</span>
# ### Statistics
# 

# %%
# Exclude 'ActivityDate' from the describe() function
Final_Merged_dataframe.drop(['ActivityDate'], axis=1).describe()


# %% [markdown]
# ##### Observation
# Statistical data were calculated for different metrics.

# %% [markdown]
# ## <span style="color: blue;">5. Share</span>

# %% [markdown]
# ### 5.1 Correlation between TotalDistance, TotalSteps, SedentaryMinutes, TotalActiveMinutes and Calories

# %% [markdown]
# A heatmap was plotted to map out the correlation between TotalDistance, TotalSteps, SedentaryMinutes, TotalActiveMinutes and Calories.

# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Assuming 'daily_activity' is already defined and contains the relevant data
# Ensure column names are correct (use strip() to remove leading/trailing spaces if needed)
Final_Merged_dataframe.columns = Final_Merged_dataframe.columns.str.strip()

# Select the relevant columns
columns_of_interest = ['TotalDistance', 'TotalSteps', 'TotalActiveMinutes', 'Calories']

# Check if all columns of interest are available in the DataFrame
missing_columns = [col for col in columns_of_interest if col not in Final_Merged_dataframe.columns]

if missing_columns:
    print(f"Missing columns: {missing_columns}")
else:
    # Create a subset with only the columns of interest
    data_subset = Final_Merged_dataframe[columns_of_interest]

    # Calculate the correlation matrix
    correlation_matrix = data_subset.corr()

    # Plot the heatmap using seaborn
    plt.figure(figsize=(8, 6))
    sns.heatmap(
        correlation_matrix,
        annot=True,
        cmap='coolwarm',  # Color palette from blue to red
        fmt=".2f",  # Format the correlation values to 2 decimal places
        linewidths=0.5,  # Add some space between the cells
        cbar_kws={"shrink": 0.8},  # Adjust color bar size
        square=True,  # Make the plot square
        annot_kws={"size": 10}  # Adjust annotation size
    )

    # Add title
    plt.title("Correlation Heatmap of Daily Activity Metrics")

    # Show the plot
    plt.show()




# %% [markdown]
# ##### Observation
# There is a positive correlation between Calories and TotalActiveMinutes (0.95), TotalSteps (0.94) and TotalDistance (0.94).

# %% [markdown]
# ### 5.2 Comparison of VeryActiveMinutes, FairlyActiveMinutes and LightlyActiveMinutes
# We next made comparison between VeryActiveMinutes, FairlyActiveMinutes and LightlyActiveMinutes. Both bar chart and pie charts were plotted.
# 
# #### 5.2.1 Bar Chart

# %%
import matplotlib.pyplot as plt

# Calculate the mean of each activity type
mean_values = Final_Merged_dataframe[['VeryActiveMinutes', 'FairlyActiveMinutes', 'LightlyActiveMinutes']].mean()

# Plotting the bar graph
plt.figure(figsize=(8, 6))
mean_values.plot(kind='bar', color=['red', 'orange', 'blue'])

# Adding labels and title
plt.xlabel('Activity Type')
plt.ylabel('Mean Minutes')
plt.title('Average Active Minutes per Activity Type')
# Remove the grid
plt.grid(False)

# Show the plot
plt.show()


# %% [markdown]
# #### 5.1.2 Pie Chart

# %%
import matplotlib.pyplot as plt

# Calculate the mean of each activity type
mean_values = Final_Merged_dataframe[['VeryActiveMinutes', 'FairlyActiveMinutes', 'LightlyActiveMinutes']].mean()

# Plotting the pie chart
plt.figure(figsize=(8, 6))
mean_values.plot(
    kind='pie', 
    autopct='%1.1f%%', 
    colors=['red', 'orange', 'blue'], 
    startangle=90, 
    wedgeprops={'edgecolor': 'black'}
)

# Adding title
plt.title('Average Active Minutes per Activity Type')

# Show the plot
plt.ylabel('')  # Hides the default ylabel
plt.show()


# %% [markdown]
# Observation: 
# Many user used more time (minutes) in Light Active Minutes (84.7%) followed by Very Active Minutes (9.3%) and Fairly Active Minutes (6.0%)

# %% [markdown]
# ### 5.2 Comparison of LightActiveDistance, ModeratelyActiveDistance and SedentaryActiveDistance
# We copared the Comparison of LightActiveDistance, ModeratelyActiveDistance and SedentaryActiveDistance by plotting bar chart.

# %%
import matplotlib.pyplot as plt

# Calculate the mean of each activity type
mean_values = Final_Merged_dataframe[['LightActiveDistance', 'ModeratelyActiveDistance', 'VeryActiveDistance', 'SedentaryActiveDistance']].mean()

# Plotting the bar graph
plt.figure(figsize=(8, 6))
ax = mean_values.plot(kind='bar', color=['orange', 'red', 'blue'])

# Adding labels on top of the bars
for i, value in enumerate(mean_values):
    plt.text(i, value + 0.05, f'{value:.2f}', ha='center', va='bottom')

# Adding labels and title
plt.xlabel('Activity Type')
plt.ylabel('Mean Distance')
plt.title('Average Active Distance by Activity Type')
# Remove the grid
plt.grid(False)

# Show the plot
plt.show()


# %% [markdown]
# ##### Observation
# Many device users participated in light activities and mostly covered light active distance followed by very active distance, moderately active distance with sedentary active distance as the last.

# %% [markdown]
# ### 5.3 Dependence of Burnt Calories on Total Active Hours
# We sought how the users' activities in terms of active hours affected the amount of the calories burned.

# %% [markdown]
# #### 5.3.1 Daily Dependence

# %%

# Plotting calories vs Total Active Hours
x = Final_Merged_dataframe['TotalActiveHours']  # Total Active Hours
y = Final_Merged_dataframe['Calories']  # Calories

# Plotting all the data points
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='black', label='Data points')

# Adding labels and title
plt.xlabel('Total Active Hours')
plt.ylabel('Total Calories')
plt.title('Calories vs Total Active Hours per Day')

# Remove the grid
plt.grid(False)

# Show the plot
plt.legend()

# %% [markdown]
# ##### Observation
# The burned calories increased by the total active hours. This is quite reasonable.

# %% [markdown]
# #### 5.3.2 Hourly Dependence

# %%

import pandas as pd
import matplotlib.pyplot as plt

# Load the daily activity dataset
daily_activity_clean = pd.read_csv('dailyActivity_merged.csv')

# Convert 'ActivityDate' to datetime format
daily_activity_clean['ActivityDate'] = pd.to_datetime(daily_activity_clean['ActivityDate'])

# Create Weekday column based on 'ActivityDate'
daily_activity_clean["WeekDay"] = daily_activity_clean["ActivityDate"].dt.day_name()

# Create new calculated columns
daily_activity_clean["TotalActiveMinutes"] = (daily_activity_clean["VeryActiveMinutes"] + 
                                        daily_activity_clean["FairlyActiveMinutes"] + 
                                        daily_activity_clean["LightlyActiveMinutes"])

daily_activity_clean["TotalMinutes"] = daily_activity_clean["TotalActiveMinutes"] + daily_activity_clean["SedentaryMinutes"]
daily_activity_clean["TotalActiveHours"] = round(daily_activity_clean["TotalActiveMinutes"] / 60)

# Assuming merged_data2 is already defined, merge with daily_activity on 'Id'
# For this example, let's assume merged_data2 is available (replace with the actual dataframe variable)
# final_merged_data = pd.merge(merged_data2, daily_activity, on='Id', how='inner')

# Define the new column order
new_cols = ["Id", "ActivityDate", 
            "WeekDay", "TotalSteps", 
            "TotalDistance", "VeryActiveDistance", 
            "ModeratelyActiveDistance", "LightActiveDistance", 
            "SedentaryActiveDistance", "VeryActiveMinutes", 
            "FairlyActiveMinutes", "LightlyActiveMinutes", 
            "SedentaryMinutes", "TotalActiveMinutes", 
            "TotalMinutes", "TotalActiveHours", "Calories"]

# Reindex the DataFrame to match the new column order
Final_Daily_Activity = daily_activity_clean.reindex(columns=new_cols)

# Plotting calories vs Total Active Hours
x = Final_Daily_Activity['TotalActiveHours']  # Total Active Hours
y = Final_Daily_Activity['Calories']  # Calories

# Plotting all the data points
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='black', label='Data points')

# Adding labels and title
plt.xlabel('Total Active Hours')
plt.ylabel('Calories')
plt.title('Calories vs Total Active Hours')

# Remove the grid
plt.grid(False)

# Show the plot
plt.legend()
plt.show()






# %% [markdown]
# ##### Observation
# The burned calories increased by the total hourly active hours. This is quite logical.

# %% [markdown]
# ### 5.4 Calories Burned dependence on Sedentary Minutes
# We next sought to investigate how sedentary minutes affected the burned calories.

# %% [markdown]
# #### 5.4.1 Daily Dependence

# %%
Final_Merged_dataframe.head(31)

# %%
import matplotlib.pyplot as plt

# Plotting the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(Final_Merged_dataframe['SedentaryMinutes'], Final_Merged_dataframe['Calories'], color='black')

# Adding labels and title
plt.xlabel('Sedentary Minutes')
plt.ylabel('Calories')
plt.title('Calories vs Sedentary Minutes')

# Remove the grid
plt.grid(False)

# Show the plot
plt.show()

# %% [markdown]
# ##### Observation
# The burned calories increased with sedentary minutes.

# %% [markdown]
# #### 5.4.2 Hourly Dependence

# %%
import matplotlib.pyplot as plt

# Plotting the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(Final_Daily_Activity['SedentaryMinutes'], Final_Daily_Activity['Calories'], color='black')

# Adding labels and title
plt.xlabel('Sedentary Minutes')
plt.ylabel('Calories')
plt.title('Calories vs Sedentary Minutes')

# Remove the grid
plt.grid(False)

# Show the plot
plt.show()



# %% [markdown]
# ##### Observation
# The hourly burned calories decreased with the total sedentary minutes.

# %% [markdown]
# ### 5.5 Calories Burned per Activity Distance
# We investigated how the calories burned depended on the active distance type.

# %% [markdown]
# #### 5.5.1 Daily Dependence

# %%
import matplotlib.pyplot as plt

# Plotting the scatter plot for each distance type
plt.figure(figsize=(12, 8))
plt.scatter(Final_Merged_dataframe['VeryActiveDistance'], Final_Merged_dataframe['Calories'], color='red', label='Very Active Distance')
plt.scatter(Final_Merged_dataframe['ModeratelyActiveDistance'], Final_Merged_dataframe['Calories'], color='orange', label='Moderately Active Distance')
plt.scatter(Final_Merged_dataframe['LightActiveDistance'], Final_Merged_dataframe['Calories'], color='green', label='Light Active Distance')
plt.scatter(Final_Merged_dataframe['SedentaryActiveDistance'], Final_Merged_dataframe['Calories'], color='purple', label='Sedentary Active Distance')

# Adding labels, title, and legend
plt.xlabel('Distance')
plt.ylabel('Calories')
plt.title('Effect of Different Activity Distances on Calories Burned')
plt.legend()

# Remove the grid
plt.grid(False)

# Show the plot
plt.show()

# %% [markdown]
# #### 5.5.2 Hourly Dependence

# %%
import matplotlib.pyplot as plt

# Plotting the scatter plot for each distance type
plt.figure(figsize=(12, 8))
plt.scatter(Final_Daily_Activity['VeryActiveDistance'], Final_Daily_Activity['Calories'], color='red', label='Very Active Distance')
plt.scatter(Final_Daily_Activity['ModeratelyActiveDistance'], Final_Daily_Activity['Calories'], color='orange', label='Moderately Active Distance')
plt.scatter(Final_Daily_Activity['LightActiveDistance'], Final_Daily_Activity['Calories'], color='green', label='Light Active Distance')
plt.scatter(Final_Daily_Activity['SedentaryActiveDistance'], Final_Daily_Activity['Calories'], color='blue', label='Sedentary Active Distance')

# Adding labels, title, and legend
plt.xlabel('Distance')
plt.ylabel('Calories Burned')
plt.title('Effect of Different Activity Distances on Calories Burned')
plt.legend()

# Remove the grid
plt.grid(False)

# Show the plot
plt.show()


# %% [markdown]
# ##### Observation
# The calories burned increased with the active distance irrespective of the type.

# %% [markdown]
# ### 5.6 Correlation between Calories Burned and Total Steps 
# We investigated how the burned calories depended on the total steps.

# %% [markdown]
# #### 5.6.1 Daily

# %%
import matplotlib.pyplot as plt

# Plotting the scatter plot for Total Steps vs. Calories
plt.figure(figsize=(10, 6))
plt.scatter(Final_Merged_dataframe['TotalSteps'], Final_Merged_dataframe['Calories'], color='black')

# Adding labels and title
plt.xlabel('Total Steps')
plt.ylabel('Burned Calories')
plt.title('Correlation between Total Steps and Calories Burned')

# Remove the grid
plt.grid(False)

# Show the plot
plt.show()

# %% [markdown]
# ### 5.6.2 Hourly Dependence

# %%
import matplotlib.pyplot as plt

# Plotting the scatter plot for Total Steps vs. Calories
plt.figure(figsize=(10, 6))
plt.scatter(Final_Daily_Activity['TotalSteps'], Final_Daily_Activity['Calories'], color='black')

# Adding labels and title
plt.xlabel('Total Steps')
plt.ylabel('Calories')
plt.title('Correlation between Total Steps and Calories Burned')
# Remove the grid
plt.grid(False)

# Remove the grid
plt.grid(False)

# Show the plot
plt.show()


# %% [markdown]
# ##### Observation
# The burned calories increased with the total steps made by the users.

# %% [markdown]
# ### 5.7 Calories Burned per Day
# We sought to investigate the day of the week when most calories were burned.

# %%
import pandas as pd
import matplotlib.pyplot as plt

# Group the data by WeekDay and sum up the total steps
calories_per_day = Final_Merged_dataframe.groupby('WeekDay', as_index=False)['Calories'].sum()

# Plot the sorted data
plt.bar(calories_per_day['WeekDay'], calories_per_day['Calories'], color="grey")
plt.xlabel("Week Day")
plt.ylabel("Total Calories Burned")
plt.title("Total Calories Burned in each Day of the Week")
# Remove the grid
plt.grid(False)
plt.xticks(rotation=30)  # Rotate labels for readability
plt.show()




# %% [markdown]
# #### Sorted in Descending Order of Total Calories Burned

# %%
import pandas as pd
import matplotlib.pyplot as plt

# Assuming merged_data1 is already created with the necessary columns

# Sort the data by Calories in descending order
daily_calories_sorted = calories_per_day.sort_values(by='Calories', ascending=False)

# Plot the sorted data
plt.figure(figsize=(10, 5))
plt.bar(daily_calories_sorted['WeekDay'], daily_calories_sorted['Calories'], color="grey")
plt.xlabel("Week Day")
plt.ylabel("Total Calories Burned")
plt.title("Total Calories Burned in each Day of the Week")
# Remove the grid
plt.grid(False)
plt.xticks(rotation=30)  # Rotate labels for readability
plt.show()


# %% [markdown]
# ##### Observation
# This plot shows that the most calories were burnt on Tuesday and that the least calories were burnt on Sunday which is understandable because the  users seem to be Christians they had not a lot of time for practice. However, Tuesday is rather strange because people seem to burn more calories than other days of the week. We needed to investigate why the users burned more calories on Tuesday.

# %% [markdown]
# ### 5.8 Total Steps Taken per Week Day
# We sought to investigate in which day of the week the users took more steps.

# %%
fig, ax = plt.subplots(figsize=(10, 5))

# Group the data by WeekDay and sum up the total steps
steps_per_day = Final_Merged_dataframe.groupby('WeekDay', as_index=False)['TotalSteps'].sum()


# Plot the bar chart with grey color
plt.bar(steps_per_day.WeekDay, steps_per_day.TotalSteps, color="grey")
plt.xlabel("Week Day")
plt.ylabel("Total Steps Taken")
plt.title("Total Steps Taken in each Day of the Week for 1 month")

# Remove the grid
plt.grid(False)
plt.xticks(rotation=30)
plt.show()




# %%
# Sort the data by Total Steps in descending order
steps_per_day_sorted = steps_per_day.sort_values(by='TotalSteps', ascending=False)

# Plot the bar chart with grey color using the sorted dataframe
plt.bar(steps_per_day_sorted.WeekDay, steps_per_day_sorted.TotalSteps, color="grey")
plt.xlabel("Week Day")
plt.ylabel("Total Steps Taken")
plt.title("Total Steps Taken in each Day of the Week for 1 month")

# Remove the grid
plt.grid(False)
plt.xticks(rotation=30)
plt.show()


# %% [markdown]
# #### Observation
# Least steps were taken on Sunday. This could explain the least Calories burnt was recorded on Sunday. This could be because the surveyed users could be Christians and spent most of their time at home or in Church praying. Similarly, most steps were taken on Tuesday and that explains why most calories were burned on that day.
# The data also gives us a clue about the profile of the users in the survey. They are most likely working class individuals.
# 

# %% [markdown]
# ### 5.9 Time Taken for Sleep per Day
# The time taked for rest (sleep) was investigated for each day of the week.

# %%
fig, ax = plt.subplots(figsize=(10, 5))

# Group the data by WeekDay and sum up the total steps
Total_minutes_asleep = Final_Merged_dataframe.groupby('WeekDay', as_index=False)['TotalMinutesAsleep'].sum()

# Plot the bar chart with grey color
plt.bar(Total_minutes_asleep.WeekDay, Total_minutes_asleep.TotalMinutesAsleep, color="grey")
plt.xlabel("Week Day")
plt.ylabel("Total Minutes Asleep")
plt.title("Total Minutes Asleep in each Day of the Week fo 1 Month")
# Remove the grid
plt.grid(False)
plt.xticks(rotation=30)
plt.show()

# %% [markdown]
# ##### Arranging in Descending order

# %%
# Sort the data by Total Minutes Asleep in descending order
Total_minutes_asleep_sorted = Total_minutes_asleep.sort_values(by='TotalMinutesAsleep', ascending=False)

# Plot the bar chart with grey color using the sorted dataframe
plt.bar(Total_minutes_asleep_sorted.WeekDay, Total_minutes_asleep_sorted.TotalMinutesAsleep, color="grey")
plt.xlabel("Week Day")
plt.ylabel("Total Minutes Asleep")
plt.title("Total Minutes Asleep in each Day of the Week for 1 Month")

# Remove the grid
plt.grid(False)
plt.xticks(rotation=30)
plt.show()


# %% [markdown]
# ##### Observation
# More hours were taken on Wednesday for sleep and least on Monday. Since more steps were taken on Tuesday and thus the amount of calories burned on that day, the users could have been tired and took more time sleeping on Wednesday.

# %% [markdown]
# ### 5.10 Time in Bed for each Day of the Month

# %%
fig, ax = plt.subplots(figsize=(10, 5))

# Group the data by WeekDay and sum up the total time in bed
Total_time_in_bed = Final_Merged_dataframe.groupby('WeekDay', as_index=False)['TotalTimeInBed'].sum()

# Sort the grouped data by Total Time in Bed in descending order
Total_time_in_bed = Total_time_in_bed.sort_values(by='TotalTimeInBed', ascending=False)

# Plot the bar chart with grey color
plt.bar(Total_time_in_bed.WeekDay, Total_time_in_bed.TotalTimeInBed, color="grey")
plt.xlabel("Week Day")
plt.ylabel("Total Time in Bed")
plt.title("Total Time in Bed in each Day of the Week for 1 Month")

# Remove the grid
plt.grid(False)
plt.xticks(rotation=30)
plt.show()


# %% [markdown]
# ##### Total Time in Bed
# Many users seem to have more time in bed on Wednesday and least on Monday. 

# %% [markdown]
# ### 5.11  Active Hours per day of the Week

# %%
fig, ax = plt.subplots(figsize=(10, 5))

# Group the data by WeekDay and sum up the total steps
Total_active_hours = Final_Merged_dataframe.groupby('WeekDay', as_index=False)['TotalActiveHours'].sum()


# Plot the bar chart with grey color
plt.bar(Total_active_hours.WeekDay, Total_active_hours.TotalActiveHours, color="grey")
plt.xlabel("Week Day")
plt.ylabel("Active Hours")
plt.title("Active Hours in each Day of the Week")
# Remove the grid
plt.grid(False)
plt.xticks(rotation=30)
plt.show()

# %%
fig, ax = plt.subplots(figsize=(10, 5))

# Group the data by WeekDay and sum up the total active hours
Total_active_hours = Final_Merged_dataframe.groupby('WeekDay', as_index=False)['TotalActiveHours'].sum()

# Sort the data by TotalActiveHours in descending order
Total_active_hours = Total_active_hours.sort_values(by='TotalActiveHours', ascending=False)

# Plot the bar chart with grey color
plt.bar(Total_active_hours.WeekDay, Total_active_hours.TotalActiveHours, color="grey")
plt.xlabel("Week Day")
plt.ylabel("Active Hours")
plt.title("Active Hours in Each Day of the Week")

# Remove the grid
plt.grid(False)
plt.xticks(rotation=30)
plt.show()

# %% [markdown]
# ##### Observation
# Tuesday was the most active day of the week and Sunday the least active day of the week.

# %% [markdown]
# ### 5.12 Comparisons of Active Distances for Each Day

# %%
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Group the data by WeekDay and sum up the distances
Very_active_distance = Final_Merged_dataframe.groupby('WeekDay', as_index=False)['VeryActiveDistance'].sum()
Moderately_active_distance = Final_Merged_dataframe.groupby('WeekDay', as_index=False)['ModeratelyActiveDistance'].sum()
Light_active_distance = Final_Merged_dataframe.groupby('WeekDay', as_index=False)['LightActiveDistance'].sum()
Sedentary_active_distance = Final_Merged_dataframe.groupby('WeekDay', as_index=False)['SedentaryActiveDistance'].sum()

# Merge the dataframes for easier plotting
activity_distances = pd.merge(Very_active_distance, Moderately_active_distance, on="WeekDay")
activity_distances = pd.merge(activity_distances, Light_active_distance, on="WeekDay")
activity_distances = pd.merge(activity_distances, Sedentary_active_distance, on="WeekDay")

# Set the plot style
sns.set(style="whitegrid")

# Plot a grouped bar chart
plt.figure(figsize=(12, 8))
bar_width = 0.2

# Create positions for each bar
positions = range(len(activity_distances))

# Plot each distance type as a bar
plt.bar(positions, activity_distances['VeryActiveDistance'], width=bar_width, label='Very Active Distance')
plt.bar([p + bar_width for p in positions], activity_distances['ModeratelyActiveDistance'], width=bar_width, label='Moderately Active Distance')
plt.bar([p + 2 * bar_width for p in positions], activity_distances['LightActiveDistance'], width=bar_width, label='Light Active Distance')
plt.bar([p + 3 * bar_width for p in positions], activity_distances['SedentaryActiveDistance'], width=bar_width, label='Sedentary Active Distance')

# Add plot labels and title
plt.xlabel('Week Day')
plt.ylabel('Activity Distance')
plt.title('Activity Distance Comparison by Weekday')
plt.xticks([p + 1.5 * bar_width for p in positions], activity_distances['WeekDay'], rotation=45)
plt.legend()

# Remove the grid
plt.grid(False)

# Show the plot
plt.show()


# %% [markdown]
# ##### Observation
# For all the days of the week, most users covered light distance followed by very active distance, moderately active distance and lastly sedentary active distance

# %% [markdown]
# ### 5.13 Comparisons of Active Distances for Each Day

# %%
import matplotlib.pyplot as plt
import seaborn as sns

# Group the data by WeekDay and sum up the Very Active Distance
Very_active_distance = Final_Merged_dataframe.groupby('WeekDay', as_index=False)['VeryActiveDistance'].sum()

# Sort the data by VeryActiveDistance in descending order
Very_active_distance = Very_active_distance.sort_values(by='VeryActiveDistance', ascending=False)

# Set the plot style
sns.set(style="whitegrid")

# Set up the figure size
plt.figure(figsize=(10, 6))

# Create the bar plot for VeryActiveDistance
sns.barplot(data=Very_active_distance, x='WeekDay', y='VeryActiveDistance', color='royalblue')

# Add plot labels and title
plt.xlabel('WeekDay')
plt.ylabel('Very Active Distance')
plt.title('Very Active Distance by Weekday (Sorted)')
plt.xticks(rotation=45)

# Remove the grid
plt.grid(False)

# Show the plot
plt.show()


# %% [markdown]
# ##### Observation
# Tuesday has the highest very active distance covered by the users. This explains why there are more active steps on Tuesday and thus supports why most calories were burned on that day.

# %% [markdown]
# #### Comparison of Minutes

# %% [markdown]
# We sought to compare the active minutes.

# %%
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Group the data by WeekDay and sum up the active minutes
Very_active_minutes = Final_Merged_dataframe.groupby('WeekDay', as_index=False)['VeryActiveMinutes'].sum()
Fairly_active_minutes = Final_Merged_dataframe.groupby('WeekDay', as_index=False)['FairlyActiveMinutes'].sum()
Lightly_active_minutes = Final_Merged_dataframe.groupby('WeekDay', as_index=False)['LightlyActiveMinutes'].sum()
Sedentary_active_minutes = Final_Merged_dataframe.groupby('WeekDay', as_index=False)['SedentaryMinutes'].sum()

# Merge all data into a single DataFrame for easier plotting
active_minutes = pd.merge(Very_active_minutes, Fairly_active_minutes, on="WeekDay")
active_minutes = pd.merge(active_minutes, Lightly_active_minutes, on="WeekDay")
active_minutes = pd.merge(active_minutes, Sedentary_active_minutes, on="WeekDay")

# Sort by Very Active Minutes for better visualization
active_minutes = active_minutes.sort_values(by='VeryActiveMinutes', ascending=False)

# Set the plot style
sns.set(style="whitegrid")

# Plot a grouped bar chart
plt.figure(figsize=(14, 8))
bar_width = 0.2
positions = range(len(active_minutes))

# Plot each type of active minutes
plt.bar(positions, active_minutes['VeryActiveMinutes'], width=bar_width, label='Very Active Minutes', color='royalblue')
plt.bar([p + bar_width for p in positions], active_minutes['FairlyActiveMinutes'], width=bar_width, label='Fairly Active Minutes', color='mediumseagreen')
plt.bar([p + 2 * bar_width for p in positions], active_minutes['LightlyActiveMinutes'], width=bar_width, label='Lightly Active Minutes', color='gold')
plt.bar([p + 3 * bar_width for p in positions], active_minutes['SedentaryMinutes'], width=bar_width, label='Sedentary Minutes', color='olive')

# Add labels and title
plt.xlabel('Week Day')
plt.ylabel('Total Minutes')
plt.title('Comparison of Active Minutes per Weekday')
plt.xticks([p + 1.5 * bar_width for p in positions], active_minutes['WeekDay'], rotation=45)
plt.legend()

# Remove the grid
plt.grid(False)

# Show the plot
plt.show()


# %% [markdown]
# ##### Observation
# Most Bellabeat device users consume more sedentary minutes and so less active. This is followed by lightly active minutes, very active minutes and lastly fairly active minutes.

# %% [markdown]
# ### 5.14 Comparison of Sedentary Minutes and Active Minutes

# %%
fig, ax = plt.subplots(figsize=(8, 5))
x = np.array(["Sedentary Minutes", "Total Active Minutes"])
y = np.array([Final_Merged_dataframe["SedentaryMinutes"].mean(),
              Final_Merged_dataframe["TotalActiveMinutes"].mean()])

plt.title("Comparison of Monthly Sedentary Minutes and Total Active Minutes")
colors = ["blue", "orange"]  # Set bar colors
plt.bar(x, y, width=0.8, color=colors)  
plt.grid(False)  # Remove the grid
plt.show()



# %% [markdown]
# #### Observation
# Most Bellabeat device users were involved in less active minutes. It is obvious that the users spend more time sitting or lying down, than they do being active. This can also reveal something about their occupation or lifestyle. Mostly likely they belong to the working class that spends most of their time behind their desks suggesting they could as well be mostly involved in online jobs.

# %% [markdown]
# ### 5.15 Active Hour of the Day

# %%
import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets
hourly_steps = pd.read_csv('hourlySteps_merged.csv')
hourly_calories = pd.read_csv('hourlyCalories_merged.csv')
daily_activity = pd.read_csv('dailyActivity_merged.csv')
sleepday = pd.read_csv('sleepDay_merged.csv')

# Ensure date columns are in datetime format
daily_activity["ActivityDate"] = pd.to_datetime(daily_activity["ActivityDate"], errors='coerce')
hourly_steps["ActivityHour"] = pd.to_datetime(hourly_steps["ActivityHour"], errors='coerce')
hourly_calories["ActivityHour"] = pd.to_datetime(hourly_calories["ActivityHour"], errors='coerce')
sleepday["SleepDay"] = pd.to_datetime(sleepday["SleepDay"], errors='coerce')

# Merge hourly steps and calories data
merge_df = pd.merge(hourly_steps, hourly_calories, on=['Id', 'ActivityHour'], how='inner')
merge_df["DateHour"] = merge_df["ActivityHour"].dt.hour

# Extract weekday names
daily_activity["WeekDay"] = daily_activity["ActivityDate"].dt.day_name()
merge_df["WeekDay"] = merge_df["ActivityHour"].dt.day_name()
sleepday["WeekDay"] = sleepday["SleepDay"].dt.day_name()

# Preview the merged DataFrame
merge_df.head()

# Plot the average steps by hour of the day
fig, axs = plt.subplots(figsize=(10, 6))
merge_df.groupby('DateHour')['StepTotal'].mean().plot(
    kind='bar', 
    rot=0, 
    ax=axs, 
    color='darkgreen',  # Set bar color to dark green
    title='The Most and Least Active Hours of the Day'
)

# Customize the plot
plt.xlabel("Hour of the Day")
plt.ylabel("Total Steps")
plt.grid(False)  # Remove the grid
plt.show()

# %% [markdown]
# #### Observation
# Here we can see that their day starts getting really busy from 6 am in the morning all the way to 10 pm in the evening. The least active hours of the day are between 11 pm to 5 am. These are probably the best hours to reach them with targeted ads.

# %% [markdown]
# ## <span style="color: blue;">6. Act</span>

# %% [markdown]
# ### 6.1 Promotion
# The data we explored revealed that consumers are less active between 11pm and 5am. This is the ideal moment for Bellabeat to schedule advertising initiatives for optimal results. Google AdWords, for example, allows internet advertisers to schedule when their adverts are shown with its ad scheduling function. Such functions can allow Bellabeat to effectively reach its consumers. Scheduling adverts will also help Bellabeat save money on advertisements.
# 
# ### 6.2 Summarized Observations
# 1.	There is a positive correlation between Calories and TotalActiveMinutes (0.95), TotalSteps (0.94) and TotalDistance (0.94).
# 2.	Many user used more time (minutes) in Light Active Minutes (84.7%) followed by Very Active Minutes (9.3%) and Fairly Active Minutes (6.0%)
# 3.	Many device users participated in light activities and mostly covered light active distance followed by very active distance, moderately active distance with sedentary active distance as the last.
# 4.	The burned calories increased by the total active hours. This is quite reasonable. The burned calories increased by the total hourly active hours. This is quite logical.
# 5.	The burned calories decreased with sedentary minutes.
# 6.	The burned calories increased with the total steps made by the users.
# 7.	The calories burned increased with the active distance irrespective of the type.
# 8.	This plot shows that the most calories were burnt on Tuesday and that the least calories were burnt on Sunday which is understandable because the  users seem to be Christians they had not a lot of time for practice. However, Tuesday is rather strange because people seem to burn more calories than other days of the week. We needed to investigate why the users burned more calories on Tuesday.
# 9.	Least steps were taken on Sunday. This could explain the least Calories burnt was recorded on Sunday. This could be because the surveyed users could be Christians and spent most of their time at home or in Church praying. Similarly, most steps were taken on Tuesday and that explains why most calories were burned on that day.
# The data also gives us a clue about the profile of the users in the survey. They are most likely working class individuals.
# 10.	More hours were taken on Wednesday for sleep and least on Monday. Since more steps were taken on Tuesday and thus the amount of calories burned on that day, the users could have been tired and took more time sleeping on Wednesday.
# 11.	Many users seem to have more time in bed on Wednesday and least on Monday.
# 12.	Tuesday was the most active day of the week and Sunday the least active day of the week.
# 13.	For all the days of the week, most users covered light distance followed by very active distance, moderately active distance and lastly sedentary active distance
# 14.	Tuesday has the highest very active distance covered by the users. This explains why there are more active steps on Tuesday and thus supports why most calories were burned on that day.
# 15.	Most Bellabeat device users consume more sedentary minutes and so less active. This is followed by lightly active minutes, very active minutes and lastly fairly active minutes.
# 16.	Most Bellabeat device users were involved in less active minutes. It is obvious that the users spend more time sitting or lying down, than they do being active. This can also reveal something about their occupation or lifestyle. Mostly likely they belong to the working class that spends most of their time behind their desks suggesting they could as well be mostly involved in online jobs.
# 17.	Here we can see that their day starts getting really busy from 6 am in the morning all the way to 10 pm in the evening. The least active hours of the day are between 11 pm to 5 am. These are probably the best hours to reach them with targeted ads.
# 
# ### 6.3 Explanation for the Observations
# 1. The positive correlation between Calories and TotalActiveMinutes, TotalSteps, and TotalDistance makes sense that burning calories aligns closely with activity levels. More movement, whether steps or distance, naturally increases calorie expenditure.
# 2. More time spent in Light Active Minutes (84.7%) shows that the Bellabeat device users engage mostly in light activity, with less time in moderate or vigorous activity. This may indicate a sedentary lifestyle or lower fitness levels.
# 3. Users cover mostly light active distance shows that there is preference for light activity that could be due to lifestyle or lack of structured workout routines.
# 4. The Calories burned increasing with total active hours shows an intuitive relationship, reinforcing the importance of staying active throughout the day.
# 5. The decreasing calories burned with sedentary minutes are due to extended sedentary periods that reduce energy expenditure, which could contribute to weight gain or other health issues.
# 6. The increase of calories burned with total steps shows that walking is a simple yet effective way to burn calories, and even small increases in step counts can improve health.
# 7. The increase of calories burned with active distance emphasizes the benefit of consistent movement.
# 8. Most calories being burned more on Tuesday and least on Sunday pattern may reflect workweek dynamics, with users more active during weekdays and resting on Sundays.
# 9. Least steps and calories burned on Sunday shows Sunday as being a low activity day, potentially linked to religious practices or rest days, reducing calorie burned.
# 10. More sleep on Wednesday, least on Monday could be due to high Tuesday activity that may lead to longer recovery sleep on Wednesday, while the transition from weekend to workweek disrupts Monday sleep.
# 11. More time in bed on Wednesday and least on Monday peoperly aligns with the previous point — users may be catching up on rest midweek.
# 12. Tuesday being the most active day is curious and worth exploring, while low Sunday activity could be linked to rest practices.
# 13. Light distance is the most common across all days shows that users favor light activity, likely due to lifestyle constraints or lack of structured fitness habits.
# 14. Highest very active distance was on Tuesday and this could explain the calorie burn spike on Tuesday — users might intentionally work out more on this day.
# 15. Users having high sedentary minutes points to prolonged periods of inactivity, possibly due to desk jobs or digital lifestyles.
# 16. Users spending more time inactive than active suggests a predominantly sedentary lifestyle may affect long-term health outcomes.
# 17. The peak activity being from 6 AM to 10 PM and least between 11 PM and 5 AM shows that Bellabeat device users follow a typical daily routine, with night hours naturally being less active.
# 
# 
# ### 6.4 Smart Device Usage
# Fitbit devices are excellent tools for tracking various aspects of daily health and fitness. The Bellabeat users used smart devices to track their steps, calories, active minutes, and sleep. By analyzing user data, we have provided valuable insights into users' activity and fitness patterns, allowing them to optimize their wellness routines and make informed decisions to enhance their overall well-being.


