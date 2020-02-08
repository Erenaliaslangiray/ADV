# **Automatic Data Visualization Tool - Idea**
_This file contains ideas and workplans of The ADV tool._

## The Idea:  
&nbsp;&nbsp;&nbsp;&nbsp;Automatic Data Visualization *(ADV)*, is a tool that will allow users to enter any kind of data to the pipeline and get the plottings of it.  
  
&nbsp;&nbsp;&nbsp;&nbsp;ADV basicly analyses the contents of a file and decices best plotting algorithms or methods to plot the data that is provided from user. Input will be analysed from all kinds aspects such as: column types, relations, data variances, means, medians etc. After, the tool will generate a metadata of input, no matter the shape of input. System will use state-of-the-art technics of Machine Learning to help itself deciding what is best while only looking the metadata. Results of desicions will be input for plotter engine which is a high-graded algorithm that can perform any kind of plotting action. Later on, users can view the results that algorithm generated within seconds with a good looking UI which they can interract with results and do one last touch on them before exporting. The last step will be the export of the results which will be prepared in a special way to preserve the means of all aspects of the data.
  
&nbsp;&nbsp;&nbsp;&nbsp;In the end, one simple tool will do all of the job that a data scientist will perform on a data to get meaningful plottings. The mission here is actually helping the individuals by not only showing what is hidden inside the data, but help them to understant it.

### **Process:**
1. Import API  
2. Input analysing  
   1. File format checker  
   2. File content checker  
      1. File datatypes checking    
      2. Language analysis & defining categorical values  
      3. Numeric data stats calculation  
   3. Metadata (Data dictionary) generating  
      1. Metadata export API  
3. Plot models selection (Metadata fed to ML models) 
4. Plotter Engine  
5. Interactive Visualizator Engine  
6. Export API

### **Design Notes on Steps:**  

1. **Import API**
  
   _Basic import api. Gets the desired data through an UI. On production, places files under S3 or other secure data storage._ 
2. **Input analysing**  
   1. **File format checker**  
     
      _Checks the validation of file format. Start with .csv and expand later on. Diversity of formats mustn't affect the tools work model since they all will end up on a same metada. Which indicates metadata generator is the adaptor for all tasks with user side._
   2. **File content checker**  
      1. **File datatypes checking**  
        
          _Checks possible problems and erros about data. Outputs can be: go or no go for entire process._
      2. **Language analysis & defining categorical values**  
        
          _NLP tools decide whether data is hierarhical or checks the context. #Cont. improvement._
      3. **Numeric data stats calculation**  
        
          _Basic datascience formulas and calculations will be applied on numerical columns to measure and identify the data and patterns of it._
   3. **Metadata** (Data dictionary) **generating**  
     
      _The most important step of the pipeline. Convert the input data to one single metadata for feeding to ML models._
      1. **Metadata Export API** (Export API can be used)  
        
          _Extra Feature: Export the metadata of the input-data to user._
3. **Plot models selection** (Metadata fed to ML models)  
  
    _ML models that gets metadata and returns the best plot options (with custom parameters) for each column of the input-data. #Cont. improvement._
4. **Plotter Engine**  
  
    _Plots the real data with the order and info provided by ML models._
5. **Interactive Visualization Engine & Display** 
  
    _An UI for user-end side of the tool. Users can edit, view and interact with the data and export the final form._
6. **Export API**  
  
    _Exports the last version of the visuals with customized templates._

### **TO-DO's:**  
*List of unordered tasks that needs to be done.*

- [x] **Import API** 
- [ ] **Input Analyse Algorithm**
    - [ ] **Input Analyse Algorithm - Research & Design**
    - [x] **Input Analyse Algorithm - File Format Check (Done at import api)** 
    - [ ] **Input Analyse Algorithm - File Datatype Checker**
    - [ ] **Input Analyse Algorithm - Language Analysis Model Build for EN**
    - [ ] **Input Analyse Algorithm - Language Analysis Model Build for TR**
    - [ ] **Input Analyse Algorithm - Language Analysis Model Integration to Pipeline**
    - [ ] **Input Analyse Algorithm - Language Analysis - Process String Input Data**
    - [ ] **Input Analyse Algorithm - Numeric Input Analyse & Calculation**
- [ ] **Metadata Generator**
- [ ] **Export API**
- [ ] **Plot Deciding Model Development**
    - [ ] **Plot Deciding Model Development - Research & Design**
    - [ ] **Plot Deciding Model Development - Data Finding**
    - [ ] **Plot Deciding Model Development - Training**
    - [ ] **Plot Deciding Model Development - Integration**
- [ ] **Plotter Engine**
    - [ ] **Plotter Engine - Research & Design**
    - [ ] **Plotter Engine - Build**
    - [ ] **Plotter Engine - Integration**
- [ ] **UI Development**
    - [ ] **UI Development - Design**
    - [ ] **UI Development - Input Page Development**
    - [ ] **UI Development - Output Page Development**
- [ ] **Export Wrapper Engine**
- [ ] **Dockerize**
    - [ ] **Dockerize - Convert to Microservice Architecture**
    - [ ] **Dockerize - Dockerfile Configuration for Each Microservice**
    - [ ] **Dockerize - Docker-Compose Configuration**
- [ ] **Log Module Implementation**
- [x] **Git Repo Design & Structure**
- [ ] **S3 Bucket Configuration**
- [ ] **Cloud DevOps - Research & Design**
- [ ] **Proof of Concept**

# **Example Datas**


```python
import pandas as pd

example_input_data = {"Id": [1,2,3,4],
                     "Size":["L","XL","S","S"],
                     "Price":[5.99,6.99,3.99,3.99],
                     "Color":["Red","Red","Red","Blue"],
                     "Weight":[200,300,150,150],
                     "Produce_Year":[2019,2018,2019,2017]}
example_metadata = {"Row_Name":["Id","Size","Price","Color","Weight","Produce_Year"],
                   "Data_Type":["int","str","int","str","int","int"],
                   "is_categorical":[0,1,0,0,0,0],
                   "is_time":[0,0,0,0,0,1],
                   "mean":[None,None,5.24,None,200,2018],
                   "variance":[None,None,1.6875,None,3750.0,0.6875]}
ml_output = {"Row_Name":["Id","Size","Price","Color","Weight","Produce_Year"],
            "Plot_Type":[None,"Histogram","Hisrogram","Piechart","Histogram","Time_series_plot"],
            "Custom_Parameters":[None,"p=2","p=3, k=9","colors=['r','b','g','o']",None,"zoom_level=3"]}
df1 = pd.DataFrame(data=example_input_data)
df2 = pd.DataFrame(data=example_metadata)
df3 = pd.DataFrame(data=ml_output)

```


```python
print("Input Data:")
df1
```

    Input Data:





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Id</th>
      <th>Size</th>
      <th>Price</th>
      <th>Color</th>
      <th>Weight</th>
      <th>Produce_Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>L</td>
      <td>5.99</td>
      <td>Red</td>
      <td>200</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>XL</td>
      <td>6.99</td>
      <td>Red</td>
      <td>300</td>
      <td>2018</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>S</td>
      <td>3.99</td>
      <td>Red</td>
      <td>150</td>
      <td>2019</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>S</td>
      <td>3.99</td>
      <td>Blue</td>
      <td>150</td>
      <td>2017</td>
    </tr>
  </tbody>
</table>
</div>




```python
print("Metadata:")
df2
```

    Metadata:





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row_Name</th>
      <th>Data_Type</th>
      <th>is_categorical</th>
      <th>is_time</th>
      <th>mean</th>
      <th>variance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Id</td>
      <td>int</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Size</td>
      <td>str</td>
      <td>1</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Price</td>
      <td>int</td>
      <td>0</td>
      <td>0</td>
      <td>5.24</td>
      <td>1.6875</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Color</td>
      <td>str</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Weight</td>
      <td>int</td>
      <td>0</td>
      <td>0</td>
      <td>200.00</td>
      <td>3750.0000</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Produce_Year</td>
      <td>int</td>
      <td>0</td>
      <td>1</td>
      <td>2018.00</td>
      <td>0.6875</td>
    </tr>
  </tbody>
</table>
</div>




```python
print("ML Output:")
df3
```

    ML Output:





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Row_Name</th>
      <th>Plot_Type</th>
      <th>Custom_Parameters</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Id</td>
      <td>None</td>
      <td>None</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Size</td>
      <td>Histogram</td>
      <td>p=2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Price</td>
      <td>Hisrogram</td>
      <td>p=3, k=9</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Color</td>
      <td>Piechart</td>
      <td>colors=['r','b','g','o']</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Weight</td>
      <td>Histogram</td>
      <td>None</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Produce_Year</td>
      <td>Time_series_plot</td>
      <td>zoom_level=3</td>
    </tr>
  </tbody>
</table>
</div>


