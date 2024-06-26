{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "for n in range(1, 51):\n",
    "    if n%3 == 0 and n%5 ==0:\n",
    "        print(f\"FizzBuzz\")\n",
    "    elif n%3 == 0:\n",
    "        print(f\"Fizz\")\n",
    "    elif n%5 == 0:\n",
    "        print(f\"Buzz\")\n",
    "    else:\n",
    "        print(n)"
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
