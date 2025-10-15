AWS Lab: 
- Deploy a simple Python backend app with docker compose on ec2 instance
- Grant permission to S3 using IAM Role
  + Use IAM role, must not use access key
- Connect to PostgreSQL RDS
  + create a RDS instance, config with best practices
- Autoscale using Auto Scaling Group (ASG)
  + scale max 3 instances, min 1
- Expose via Application Load Balancer (ALB)
- Domain task: 
    + Move test.<domain cua m> domain to route53 
    + add DNS: thang19.test.<domain> to the app
- Advanced task: add ssl to your app, using ACM certificate. (don't export certificate, it will cost 15$)
####