{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e49ce337",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "\n",
    "def preprocess_data(data_path):\n",
    "    df = pd.read_csv(data_path, sep=\";\", encoding=\"ansi\")\n",
    "\n",
    "    return df\n",
    "\n",
    "def scale_data(data):\n",
    "    scaler = StandardScaler()\n",
    "    scaled_data = scaler.fit_transform(data)\n",
    "    return scaled_data\n"
   ]
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
