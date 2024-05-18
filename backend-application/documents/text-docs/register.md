## Register User



Fields : 

    username : string : unique
    email : string : unique
    mobile : integer : unique
    password : string 
    active_status : boolean
    

**Types of Registration :** 
1. Using email address
2. Using Mobile number
3. Using Social Media Account

**Using Email Address :**
- input email address
- if entered email id is valid then send otp on entered email address
    - input otp which sent on email which client entered
    - if otp is match
        - set password for user
        - create profile in database and activate account
    - else
        - resend otp button send otp again on inputed email id
        - change email address enable to edit inputed email address 
- else email invalid input correct email id

**Using Mobile Number :**
- input mobile number
- if entered mobile number is valid then send otp on entered mobile number
    - input otp which sent on mobile number which client entered
    - if otp is match
        - set password for user
        - create profile in database and activate account
    - else
        - resend otp button send otp again on inputed mobile number
        - change mobile number enable to edit inputed number 
- else mobile number invalid input correct mobile number

**Using Social Media Account :**
- select social media icon which you want to use for registration
- social auth service run and validate the social credentials 
- ask to set password 
- save profile in database and activate

