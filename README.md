# Sprinklr API Consumption through Data Engine 
Simple example of data ingestion into Sprinklr via SFTP Server and Data Engine. In this instance, this will pull in data on the hourly consumption of the Sprinklr API:

```
git clone https://github.com/jonjakk/Sprinklr-Data-Engine-Ingestion
```
Edit username/passwords in the docker compose file and get working Sprinklr API credentials.
```
cd Sprinklr-Data-Engine-Ingestion
```
```
mkdir exampleuser/upload
```
```
sudo docker compose build && sudo docker compose up
```


Check out the offical Data Engine Documentation here: [‎About the Data Engine ](https://www.sprinklr.com/help/articles/data-flow/about-the-data-engine/63f84bfc9b334f7283b4dc8d)


**Notes:**

-   This project is not created by, or supported by Sprinklr. Please review the library before using in a production environment to make sure it meets your organization's security and compliance requirements!
