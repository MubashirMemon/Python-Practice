{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Marksheet\n",
      "Enter English Marks : 90\n",
      "Enter Maths Marks : 87\n",
      "Enter Physics Marks : 78\n",
      "Enter Chemistry Marks : 76\n",
      "Enter Management Marks : 56\n",
      "Total Marks 387\n",
      "77.4\n",
      "Grade B\n"
     ]
    }
   ],
   "source": [
    "#task 1\n",
    "print (\"Marksheet\")\n",
    "sub1= int(input(\"Enter English Marks : \"))\n",
    "sub2= int(input(\"Enter Maths Marks : \"))\n",
    "sub3= int(input(\"Enter Physics Marks : \"))\n",
    "sub4= int(input(\"Enter Chemistry Marks : \"))\n",
    "sub5= int(input(\"Enter Management Marks : \"))\n",
    "Total_Marks = (sub1+sub2+sub3+sub4+sub5)\n",
    "print (\"Total Marks\",Total_Marks)\n",
    "per = (sub1+sub2+sub3+sub4+sub5)/5\n",
    "print (per)\n",
    "if(per>=80):\n",
    "    print (\"Grade A\")\n",
    "elif (per>=70):\n",
    "    print (\"Grade B\")\n",
    "elif (per>=60):\n",
    "    print (\"Grade C\")\n",
    "elif (per>=50):\n",
    "    print (\"Grade D\")\n",
    "else: \n",
    "    print (\"Grade F\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number67\n",
      "67 is Odd number : \n"
     ]
    }
   ],
   "source": [
    "#task 2\n",
    "number = int(input (\"Enter a number\"))\n",
    "remainder = number % 2 \n",
    "if (remainder == 0):\n",
    "    print (number, \" is an Even number : \")\n",
    "else:\n",
    "    print (number, \"is Odd number : \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The length of list is:  5\n"
     ]
    }
   ],
   "source": [
    "#task 3\n",
    "n = len([10, 20, 30,70,56]) \n",
    "print(\"The length of list is: \", n) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "19\n"
     ]
    }
   ],
   "source": [
    "#task 4\n",
    "list = [1,2,3,4,9]\n",
    "total = sum(list)\n",
    "print (total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12\n"
     ]
    }
   ],
   "source": [
    "#task 5\n",
    "def sum_list(numeric):\n",
    "    sum_numbers = 0\n",
    "    for x in numeric:\n",
    "        sum_numbers += x\n",
    "    return sum_numbers\n",
    "print(sum_list([1,2,9]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 1, 2, 3, 5]\n"
     ]
    }
   ],
   "source": [
    "#task 6\n",
    "a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]\n",
    "list_number_less_than_5 = a[0 :5]\n",
    "print (list_number_less_than_5)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
