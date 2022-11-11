{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d33e5579",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the length of password :15\n",
      "л$ⴳMēûüwZįåóFⵎю\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "passlen = int (input(\"enter the length of password :\"))\n",
    "s= \"absdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ!@#$%âæáäãåāªéèêëęėēûùüúūîïìíįīôœöòóõõøōçćčñń‰≠≈¥¿¡§€;₩₽ⵉⵣⵎⴰⵡⴻⵏⵏⴳⴻⵔⴳⴻцгшщзфвалджэсбю\"\n",
    "p= \"\".join(random.sample(s,passlen))\n",
    "print(p)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cb8931ff",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
