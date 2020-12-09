{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Twinkle, twinkle, little star,\n",
      "       How I wonder what you are!\n",
      "            Up above the world so high,\n",
      "            Like a diamond in the sky.\n",
      "Twinkle, twinkle, little star,\n",
      "       How I wonder what you are\n"
     ]
    }
   ],
   "source": [
    "print (\"Twinkle, twinkle, little star,\")\n",
    "print (\"       How I wonder what you are!\")\n",
    "print (\"            Up above the world so high,\")\n",
    "print (\"            Like a diamond in the sky.\")\n",
    "print (\"Twinkle, twinkle, little star,\")\n",
    "print (\"       How I wonder what you are\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Python Version\n",
      "3.7.4 (default, Aug  9 2019, 18:34:13) [MSC v.1915 64 bit (AMD64)]\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "print (\"Python Version\")\n",
    "print (sys.version)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Current date and time\n",
      "2019-10-31 11:22:55\n"
     ]
    }
   ],
   "source": [
    "import datetime\n",
    "now= datetime.datetime.now()\n",
    "print (\"Current date and time\")\n",
    "print (now.strftime(\"%Y-%m-%d %H:%M:%S\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter radius of circle: 5\n",
      "Area of the circle:\n",
      "78.5\n"
     ]
    }
   ],
   "source": [
    "r =float(input(\"Enter radius of circle: \"))\n",
    "PI = 3.14\n",
    "area = PI*r**2\n",
    "print (\"Area of the circle:\")\n",
    "print(area)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter user first name:  Mubashir\n",
      "Enter user second name: Memon\n",
      "Memon Mubashir\n"
     ]
    }
   ],
   "source": [
    "string1= input(\"Enter user first name:  \")\n",
    "string2= input (\"Enter user second name: \")\n",
    "string3= string2 +' '+ string1\n",
    "print (string3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter value 1: 56\n",
      "Enter value 2: 4\n",
      "60\n"
     ]
    }
   ],
   "source": [
    "x= input (\"Enter value 1: \");\n",
    "y= input (\"Enter value 2: \");\n",
    "z= int (x) + int (y)\n",
    "print(z);"
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
