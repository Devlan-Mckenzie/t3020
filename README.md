 
# T3020   Repo for ELEN3020

Name:Devlan McKenzie
Date: 7 June


# Description of code -- for question 1.1 and 1.2

The program `datamunger.py` is used to quality check data files. A
sample data file is given. The first row consists of headings which
the program ignores. The quality checks are

* The column TALL should be the sum of T1 through T8 inclusive
* For each of columns TALL and T1 through T7 inclusive (not T8),  the values increase monotonically. For example if in row 13, column T3 there's a value 49 (for example), then in row 14, column T3 the value should be 49 or greater.

Note, however, there is some missing data in some of the rows. The first few lines only contain values for TALL and only the latter half has values for OTHER.  If there are missing data for any row in columns TALL and T1 through T8 then that row should not be checked. However, we keep track of how many rows there are with missing data


### Errors

There are three deliberate errors, marked E1, E2 and E3. Finding other (non-deliberate and unknown to me)  errors will get a bonus -- clearly add below this line in your copy of the README what the errors are and how you fixed them.

E1 - changed the "for c in curr[2:9]" into "for c in curr[1:9]" this is so that T1 is included.
E2 - changed the "for i in range(9)" into "for i in range(8)" this is because T8 does not follow monotonically behaviour as stated in the Readme.
   - changed the "if curr[i] <= prev[i]" into "if curr[i] < prev[i]" this was because the monotonical behaviuor was able to be equal or greater than the previous, this would show an error if they were equal and it is now fixed.
E3 - changed the "for d in curr_str" into "for d in curr_str[0:9]" this was because the curr_str was an array of sorts and thus requires an index to access its elements.
