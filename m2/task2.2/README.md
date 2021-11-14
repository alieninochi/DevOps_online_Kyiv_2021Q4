# Task 2.2

***

1. I've created Lightsail instance: 

![](./images/image1.png)

![](./images/image2.png)

Instance is ready and already running:

![](./images/image3.png)

I've connected to the instance through puTTY on my local machine:

![](./images/image4.png)

2. I've created EC2 instance, for OS was chosen CentOS 6.

![](./images/image5.png)

This instance in list of all instances:

![](./images/image6.png)

Connecting to the instance through puTTY:

![](./images/image7.png)

3. I've made snapshot of this instance:

![](./images/image8.png)

4. I've created EBS volume:

![](./images/image9.png)

and attached it to my CentOS instance, mounted it and created new file:

![](./images/image10.png)

![](./images/image11.png)

5. I've created OS image based on snapshot that I've made in previous steps.

In "Launch instance" I choose "My AMIs" and create instance the same as instances from AWS AMIs.

![](./images/image12.png)

![](./images/image13.png)

6. I've detached Disk_D from first inctance and attached it for instance from snapshot:

![](./images/image14.png)

7. I've created Lightsail Wordpress instance:

![](./images/image15.png)

Administrator's panel:

![](./images/image16.png)

I've attached static IP to instance:

![](./images/image17.png)

and made DNS record for my domain:

![](./images/image18.png)

Site works on this domain:

![](./images/image19.png)

8. Work with S3:

- Create bucket:

![](./images/image20.png)

- Upload files to bucket:

![](./images/image21.png)

9. Work with S3 through command line:

I've created new user in IAM:

![](./images/image22.png)

I've created file on local machine and uploaded it to my bucket:

![](./images/image23.png)

File appeared in bucket:

![](./images/image24.png)

10. Docker Container Deployment on Amazon ECS:

Creating cluster:

![](./images/image25.png)

Running demo app:

![](./images/image26.png)

11. [My link to a static website with my AWS completed labs](http://zoeholubkovainfo.s3-website.eu-central-1.amazonaws.com/)