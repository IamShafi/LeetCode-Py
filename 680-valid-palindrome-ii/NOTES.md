Check if the leftmost & rightmost character are same or not.
{
while l<r
}
IF not, then delete 1 character.
delete leftmost: s[ l+1 : r+1 ]
check palindrom
delete rightmost: s[ l : r ]
check palindrom
​
case: abc == false, we cant delete any.
l & r pointer are not same
​