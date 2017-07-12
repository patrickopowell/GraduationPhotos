# Functional Overview  
The proof finder searches a selection of potential graduation images.  These images are free of any watermarking, and publicly accessible by anyone.  This application loops through universities/departments, picture locations, and individual pictures.  A small test of this application yielded 75,000 publicly accessible, watermark-free images.

# Organization  
The search mechanics are organized based on components of unique identifiers.  
* University/Department Identifier  
  * This 8-digit code uniquely identifies the university or department for which the ceremony is taking place.  Due to the limited resources of a personal computer, I only checked for 3 million universities/departments.
* Picture Location Identifier
  * This 5-digit code uniquely identifies the location the picture was taken (stage, flag, etc...).  For this analysis, I only checked for 2 picture locations.
* Student Identifier
  * This 4-digit code uniquely identifies the student for whom the picture was taken.  For this analysis, I only checked the first 500 pictures of each graduation ceremony.

# Resources
* [My First Graduation Photo](https://www.photospecialties.com/Images/Graduation/2017/26993244/00001/0256.jpg)
* [My Second Graduation Photo](https://www.photospecialties.com/Images/Graduation/2017/26993244/00002/0217.jpg)
* [Photo Specialties Contact](https://www.photospecialties.com/Graduation/OrderingMobile/Utilities/ContactUs.asp)