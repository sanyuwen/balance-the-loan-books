in my program, there are those classes:

0. Bank: represents a bank. bank has its id, name, 
         and keeps track of all facilities under it.
1. DataStore: data access layer. read/write data sources. 
              it also keep track of assignments along the way.
2. Facility: represents a facility of a particular bank. 
             has id, associated bank id, interest, current remaining amount, maximum allowed default likelihood,
             banned_states, already assigned loans under this facility, total amount those loans exptected yields
3. Loan: represents a loan
4. Dispatcher: dispatch method to assign each newly arrived loan to specific facility.
               it filters out qualified facilities based on default likelihood, banned states and current remaining amount
               then it selects the facility which will yield maxinum profit and assign to it

and there are 2 additional files:
0. balance_the_loan_books.py: restful api endpoints: http://127.0.0.1:5000/assign-loan which will receive newly arrived 
                              loan from a post call (streaming process). http://127.0.0.1:5000/export, get call will export
                              all assignments and yields for all currently processed loans.
1. Test_test_balance_the_loan_books.py: unit test, all code is self explatory.

1. How long did you spend working on the problem? What did you find to be the most difficult part?
ans: 
3 hours to design and write the code. 1 hour to wirte this additional comments/write up
not very difficult given such simplified model

2. How would you modify your data model or code to account for an eventual introduction of new, 
as-of-yet unknown types of covenants, beyond just maximum default likelihood and state restrictions?
ans:
i would modify my Facility class utilized https://en.wikipedia.org/wiki/Specification_pattern
whereby business rules can be recombined by chaining the business rules together using boolean logic
since the covenants are some boolean logic. if want to add more covenants, Specification_pattern will
chain those boolean logic which make it more maitainable.

3. How would you architect your solution as a production service wherein new facilities can be introduced 
at arbitrary points in time. Assume these facilities become available by the finance team emailing your 
team and describing the addition with a new set of CSVs.
ans:
my current implementation can be added more facilities at arbitrary points in time. user can change the data source
when new facility comes in.

4. Your solution most likely simulates the streaming process by directly calling a method in your code 
to process the loans inside of a for loop. What would a REST API look like for this same service? 
Stakeholders using the API will need, at a minimum, to be able to request a loan be assigned to a 
facility, and read the funding status of a loan, as well as query the capacities remaining in 
facilities. 
ans:
my code (balance_the_loan_books.py) supports this.

5. How might you improve your assignment algorithm if you were permitted to assign loans 
in batch rather than streaming? We are not looking for code here, but pseudo code or description of 
a revised algorithm appreciated. 
ans:
Test_test_balance_the_loan_books.py supports this.

6. Discuss your solution’s runtime complexity
ans:
assume stream processing:
dispatch run O(N) time. N = number of facilities in place

assume batch processing:
the whole process run O(N*M). N = number of facilities in place, M = number of loans in the batch