{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 파이썬을 이용한 머신러닝, 딥러닝 실전 앱 개발 \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 문자인식 - 손글씨 숫자 판정하기"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "* dataset = 8 x 8 픽셀의 손글씨 숫자 데이터 5620개"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAV0AAADxCAYAAABoIWSWAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy8QZhcZAAAUoUlEQVR4nO3df6zddX3H8deLlohS6Y9tkk23FgjOH3O9SP+aYb1kMCaLuWUOgz+wJZo1EExL3NL+gfEWXaSJWdsoKiSEVjEmmGDrxMyo0GaabJOm7RIiq05uAaXx1+2VFqgO3/vj3GZdw/f9pd/b8/l8b+/zkdwI9805532+5/t93+855+Xn64gQAKCMc2o3AABzCUMXAApi6AJAQQxdACiIoQsABTF0AaAghi4AFNSboWt7ie2v2D5m+5Dt99TuqTbbt9p+1PZx29tr99MHtl9h+97pfeRZ2/tsv712X7XZvt/2M7Z/Zfug7Q/W7qkvbF9q+wXb99fuRZLm127gJHdJ+rWkCyWNSHrI9oGIeKxuW1X9RNLHJV0j6ZWVe+mL+ZKekrRS0pOSrpX0gO23RMREzcYq+4SkD0TEcdtvkLTb9r6I2Fu7sR64S9L3ajdxQi/OdG2fL+mdkj4SEUcj4juSvirpxrqd1RURD0bETkm/qN1LX0TEsYgYj4iJiPhtRHxN0hOSLq/dW00R8VhEHD/xr9M/l1RsqRds3yDpiKRv1+7lhF4MXUmvl/RiRBw86XcHJL25Uj+YJWxfqMH+M5ffEUmSbH/G9nOSHpf0jKSvV26pKtsXSLpD0odr93KyvgzdBZKmTvndlKRXV+gFs4TtcyV9UdKOiHi8dj+1RcQtGhwzV0h6UNLx/BZnvY9JujcinqrdyMn6MnSPSrrglN9dIOnZCr1gFrB9jqQvaPA9wK2V2+mNiHhx+uO510m6uXY/tdgekXSVpC21ezlVX75IOyhpvu1LI+IH079bLt4y4iXYtqR7NfjS9dqI+E3llvpovub2Z7qjkpZJenKwu2iBpHm23xQRb63YVz/OdCPimAZvh+6wfb7tt0ka0+BMZs6yPd/2eZLmabDDnGe7L38oa/qspDdKekdEPF+7mdpsv8b2DbYX2J5n+xpJ75b0cO3eKrpHgz86I9M/n5P0kAZJoKp6MXSn3aJBLOqnkr4k6eY5HheTpNslPS9po6T3Tf/z7VU7qsz2UklrNTiQDts+Ov3z3sqt1RQafJTwtKRJSZ+UtD4idlXtqqKIeC4iDp/40eAjzBci4me1ezOLmANAOX060wWAsx5DFwAKYugCQEEMXQAoiKELAAWlmU/bnaIN119/fVq/8847G2vf+ta3GmsbN25srE1OTrY31iAi/HL/267bpM3u3bsba4sWLWqsffSjH22s7drVPTF0OttEGt52GR0dbazt3LmzsbZ///5O99mmxL6yYcOGtJ4dPz/60Y8aaytWrGiszfbjJztGtm/f3lhbtWrVELrJtwlnugBQEEMXAApi6AJAQQxdACiIoQsABQ1lxars21VJuvjiixtrixcvbqz98pe/bKy9613vSh/zy1/+clqv7ciRI421lStXNtauvPLKxtpM0guljIyMpPVHHnmksTY1deq69/9n2bJlXVsqIjtG2tI/a9eubazdfffdjbXLL2++olGWGpoN1qxZ01jLkiw1cKYLAAUxdAGgIIYuABTE0AWAghi6AFAQQxcACuocGcviJ1kkTJIuuaT5IqXZgh3f/OY3O/Uj1Y+MtUWjui7C0rc4zOlqW3DkwIEDjbVswZtsIaA+uOeeexprmzdvTm/76KOPNtay42c2x8KyBW2kPDK2devWxtpMooUTExOdbseZLgAUxNAFgIIYugBQEEMXAApi6AJAQQxdACiIoQsABXXO6WZLMO7duze9bZYlzLTdb23r169vrI2Pj6e3XbhwYafHzC5oORtkGUopz0Jmt+37spbZMdCWc8/qWRY3O2ZncmHKErIcrpTnbbMLU2b7ULbcqtR+TDfhTBcACmLoAkBBDF0AKIihCwAFMXQBoCCGLgAUNJTI2LCWkOt75CWLn2SxFal7/21L3vVB1mMWs5Pal35s0hYx6rO2SOWSJUsaa9nyp1nt6quvTh+zxPE1NjbWWNuyZUt62x07dnR6zHXr1jXWbrrppk732YYzXQAoiKELAAUxdAGgIIYuABTE0AWAghi6AFBQ58hYFiFpuzJvJouFZfdb+2q/tWRXGe7LlYKz1ZiyyE6bLE7WtkLUbJYde1n06+67726sbdiwIX3MjRs3tjc2Q1NTU51qkrR69erGWtuVuJtkV5ueCc50AaAghi4AFMTQBYCCGLoAUBBDFwAKYugCQEGdI2PZSkhtkbHrr7++Uy2zefPm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\n",
      "text/plain": [
       "<Figure size 432x288 with 15 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "#손글씨 데이터 읽어 들이기 \n",
    "from sklearn import datasets\n",
    "\n",
    "digits = datasets.load_digits()\n",
    "\n",
    "#15개만 출력해 보기\n",
    "for i in range(15):\n",
    "    plt.subplot(3, 5, i+1)\n",
    "    plt.axis('off')\n",
    "    plt.title(str(digits.target[i]))\n",
    "    plt.imshow(digits.images[i], cmap = 'gray')\n",
    "\n",
    "plt.show() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 0.  0. 12. 10.  0.  0.  0.  0.]\n",
      " [ 0.  0. 14. 16. 16. 14.  0.  0.]\n",
      " [ 0.  0. 13. 16. 15. 10.  1.  0.]\n",
      " [ 0.  0. 11. 16. 16.  7.  0.  0.]\n",
      " [ 0.  0.  0.  4.  7. 16.  7.  0.]\n",
      " [ 0.  0.  0.  0.  4. 16.  9.  0.]\n",
      " [ 0.  0.  5.  4. 12. 16.  4.  0.]\n",
      " [ 0.  0.  9. 16. 16. 10.  0.  0.]]\n"
     ]
    }
   ],
   "source": [
    "d0 = digits.images[5]\n",
    "plt.imshow(d0, cmap= 'gray')\n",
    "plt.show()\n",
    "print(d0)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 이미지 머신러닝"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.9511111111111111\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\student\\Anaconda3\\lib\\site-packages\\sklearn\\svm\\base.py:929: ConvergenceWarning: Liblinear failed to converge, increase the number of iterations.\n",
      "  \"the number of iterations.\", ConvergenceWarning)\n"
     ]
    }
   ],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn import datasets, svm, metrics\n",
    "from sklearn.metrics import accuracy_score\n",
    "\n",
    "# 데이터 읽어 들이기 --- (*1)\n",
    "digits = datasets.load_digits()\n",
    "x = digits.images\n",
    "y = digits.target\n",
    "x = x.reshape((-1, 64)) # 2차원 배열을 1차원 배열로 변환하기 --- (*2)\n",
    "# 데이터를 학습 전용과 테스트 전용으로 분리하기 --- (*3)\n",
    "x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)\n",
    "\n",
    "# 데이터 학습하기 --- (*4)\n",
    "clf = svm.LinearSVC()\n",
    "clf.fit(x_train, y_train)\n",
    "\n",
    "# 예측하고 정답률 출력하기 --- (*5)\n",
    "y_pred = clf.predict(x_test)\n",
    "print(accuracy_score(y_test, y_pred))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 학습데이터 저장"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['digits.pkl']"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "joblib.dump(clf, 'digits.pkl')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 학습한 데이터 읽기\n",
    "clf = joblib.load('digits.pkl')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 이미지 판정하기"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "https://firealpaca.com/kr/\n",
    "* 해당링크 다운 후 에서 직접 그려서 저장 후 판정해보기(두껍게, 정중앙으로)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2.png = 2\n",
      "4.png = 4\n"
     ]
    }
   ],
   "source": [
    "import cv2\n",
    "from sklearn.externals import joblib\n",
    "\n",
    "def predict_digit(filename):\n",
    "  # 학습한 데이터 읽어 들이기\n",
    "    clf = joblib.load(\"digits.pkl\")\n",
    "    # 직접 그린 손글씨 이미지 읽어 들이기\n",
    "    my_img = cv2.imread(filename)\n",
    "    # 이미지 데이터를 학습에 적합하게 변환하기\n",
    "    my_img = cv2.cvtColor(my_img, cv2.COLOR_BGR2GRAY)\n",
    "    my_img = cv2.resize(my_img, (8, 8))\n",
    "    my_img = 15 - my_img // 16 # 흑백 반전\n",
    "    # 2차원 배열을 1차원 배열로 변환하기\n",
    "    my_img = my_img.reshape((-1, 64))\n",
    "    # 데이터 예측하기\n",
    "    res = clf.predict(my_img)\n",
    "    return res[0]\n",
    "\n",
    "# 이미지 파일을 지정해서 실행하기\n",
    "n = predict_digit(\"2.png\")\n",
    "print(\"2.png = \" + str(n))\n",
    "n = predict_digit(\"4.png\")\n",
    "print(\"4.png = \" + str(n))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 윤곽검출"
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
      "97 64 30 28\n",
      "101 9 90 81\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import cv2\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# 이미지 읽어 들이고 크기 변경하기 --- (*1)\n",
    "img = cv2.imread(\"flower.jpg\")\n",
    "img = cv2.resize(img, (300, 169))\n",
    "\n",
    "# 색공간 변경하기 --- (*2)\n",
    "gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)\n",
    "gray = cv2.GaussianBlur(gray, (7, 7), 0) \n",
    "im2 = cv2.threshold(gray, 140, 240, cv2.THRESH_BINARY_INV)[1]\n",
    "# 화면 왼쪽에 변환한 이미지 출력하기 --- (*3)\n",
    "plt.subplot(1, 2, 1)\n",
    "plt.imshow(im2, cmap=\"gray\")\n",
    "\n",
    "# 윤곽 검출하기 --- (*4)\n",
    "cnts = cv2.findContours(im2, \n",
    "        cv2.RETR_LIST,\n",
    "        cv2.CHAIN_APPROX_SIMPLE)[1]\n",
    "# 검출한 윤곽 그리기 --- (*5)\n",
    "for pt in cnts:\n",
    "    x, y, w, h = cv2.boundingRect(pt)\n",
    "    # 너무 크거나 너무 작은 부분 제거하기\n",
    "    if w < 30 or w > 200: continue\n",
    "    print(x,y,w,h) # 결과 출력하기\n",
    "    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)\n",
    "\n",
    "# 화면 오른쪽에 결과 출력하기\n",
    "plt.subplot(1, 2, 2)\n",
    "plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))\n",
    "plt.savefig(\"obj1.png\", dpi=200)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 'hagaki1 이미지 출력해보기'\n",
    "(책에 없으나, 아래 코드를 이해하는데 도움됨, 생략해도 무관)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import cv2\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "img = cv2.imread(\"hagaki1.png\")\n",
    "\n",
    "plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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ajym0jSJcHkh1ph81H8W/9rXwvRpHytKgajYcy9ax0T7RjLq5/6qT4cewq16XKgtkqspRIAvfCGthjpEolK/nuaUKFf5lYmPkSgiphjewCfHX150SYUQy2lpaUl6HgXRHBKDS0qvVOeRhlJ89erVA97fhz/84Z6dfM90Nhe3AkW0rBQUAfXdFX2zTz75ZM14yxfiqtmXO9jmlIT5rxUkVcn+Mv7cuXO56qqrAJg/f37lQV8pbsHhI/p866WmWQ7yMoZ4BOf8jXoxDjcrVqzgzjvv7PecSy+9tK645s2bV7PX7d/+7d9K56RP9sFQnflXrVrFY48N+MZbv3zmM5/h05/+NLfffjurV6+ueBNmsIgI69evL+1Pmzatn7NfuZgYG8w555xTsf/444/3yoy33377kNL45Cc/OaTraxFFEccffzwLFy7kjDPOGHQ81157Lddddx3vf//7mTdv3pDtqn5gvOMd72D79u11Xfvoo49W7Jc/0LLIqG8zDifVnQS33norJ554IgCtra10dXU12QIpVSmLUiT8vF3lh5Gkul5RvaWyXffggw822c76qBbi8uXLeetb31r39d/+dn0PvY9//OMHZVezsJKxgSxYsKC0feqpp7J06dLS/nvf+96GpdN320rQtIXrugEPrWXnqg+uBKis3p5yyikNs23p0qUsXbqUG2+8cUjxnHVW5QSve++996CECGHIphbr1q2r2O/pIxhZTIwNJq0G/frXv64Ib2sb+rr4H/vYx3oJsbwtJWUTMSOfJy446Oyp/KgPP/dpp51WEcdvfvObIduWsmzZMpYtW8ZHPvKRQXn4Ati+fTsPPPBAaf8b3/gG55577kHHU17al3P++Y2ZBNFoTIzDxE033TToa9NM/eUvf7ki/KGHHur1YnY6a8R3HcDv3klx77ayeHquS6m3M2koHKwgq99vveKKK1i7du1Bp/v5z/+/muH19FKPBCbGYeBA1TS3Rr1Mfe2111YGKGEBN6D7G7fx0mUX89Kll5QOp2Og5dx22229wtIxzHpZuXIlF198MXfffTf3338/999/P7NnD261lQsuuKBm+LHHHst11113UHGNTxYae+ihh/rstDnzzDNrho8EJsYm093dzbhxlW+LbNmy5aDiqK7ypvzsZz8rzWxJSafydU6eTHHyYRRmHF46piq8+93vrjy/RlVy3759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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import cv2\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# 엽서 이미지에서 우편 번호를 추출하는 함수\n",
    "def detect_zipno(fname):\n",
    "    # 이미지 읽어 들이기\n",
    "    img = cv2.imread(fname)\n",
    "    # 이미지 크기 구하기\n",
    "    h, w = img.shape[:2]\n",
    "    # 이미지의 오른쪽 윗부분만 추출하기 --- (*1)\n",
    "    img = img[0:h//2, w//3:]\n",
    "    \n",
    "    # 이미지 이진화하기 --- (*2)\n",
    "    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)\n",
    "    gray = cv2.GaussianBlur(gray, (3, 3), 0) \n",
    "    im2 = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY_INV)[1]\n",
    "    \n",
    "    # 윤곽 검출하기 --- (*3)\n",
    "    cnts = cv2.findContours(im2, \n",
    "        cv2.RETR_LIST,\n",
    "        cv2.CHAIN_APPROX_SIMPLE)[1]\n",
    "    \n",
    "    # 추출한 이미지에서 윤곽 추출하기--- (*4)\n",
    "    result = []\n",
    "    for pt in cnts:\n",
    "        x, y, w, h = cv2.boundingRect(pt)\n",
    "        # 너무 크거나 너무 작은 부분 제거하기 --- (*5)\n",
    "        if not(50 < w < 70): continue\n",
    "        result.append([x, y, w, h])\n",
    "    # 추출한 윤곽을 위치에 따라 정렬하기 --- (*6)\n",
    "    result = sorted(result, key=lambda x: x[0])\n",
    "    # 추출한 윤곽이 너무 가까운 것들 제거하기 --- (*7)\n",
    "    result2 = []\n",
    "    lastx = -100\n",
    "    for x, y, w, h in result:\n",
    "        if (x - lastx) < 10: continue\n",
    "        result2.append([x, y, w, h])\n",
    "        lastx = x\n",
    "    # 초록색 테두리 출력하기 --- (*8)\n",
    "    for x, y, w, h in result2:\n",
    "        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)\n",
    "    return result2, img\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    # 이미지를 지정해서 우편번호 추출하기\n",
    "    cnts, img = detect_zipno(\"hagaki1.png\")\n",
    "\n",
    "    # 결과 출력하기 --- (*7)\n",
    "    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))\n",
    "    plt.savefig(\"detect-zip.png\", dpi=200)\n",
    "    plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 바로위 코드만 detect_zip.py으로 저장하기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 추출한 숫자 이미지 판정하기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-23-7b6e2141cfa8>, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-23-7b6e2141cfa8>\"\u001b[1;36m, line \u001b[1;32m1\u001b[0m\n\u001b[1;33m    from detect-zip import *\u001b[0m\n\u001b[1;37m               ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "from detect_zip import *\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "from sklearn.externals import joblib\n",
    "\n",
    "# 학습한 데이터 읽어 들이기\n",
    "clf = joblib.load(\"digits.pkl\")\n",
    "\n",
    "# 이미지에서 영역 읽어 들이기\n",
    "cnts, img = detect_zipno(\"hagaki1.png\")\n",
    "\n",
    "# 읽어 들인 데이터 출력하기\n",
    "for i, pt in enumerate(cnts):\n",
    "    x, y, w, h = pt\n",
    "    # 윤곽으로 감싼 부분을 작게 만들기\n",
    "    x += 8\n",
    "    y += 8\n",
    "    w -= 16\n",
    "    h -= 16\n",
    "    # 이미지 데이터 추출하기\n",
    "    im2 = img[y:y+h, x:x+w]\n",
    "    # 데이터를 학습에 적합하게 변환하기\n",
    "    im2gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY) # 그레이스케일\n",
    "    im2gray = cv2.resize(im2gray, (8, 8)) # 크기 변경\n",
    "    im2gray = 15 - im2gray // 16 # 흑백 반전\n",
    "    im2gray = im2gray.reshape((-1, 64)) # 차원 변환\n",
    "    # 데이터 예측하기\n",
    "    res = clf.predict(im2gray)\n",
    "    # 출력하기\n",
    "    plt.subplot(1, 7, i + 1)\n",
    "    plt.imshow(im2)\n",
    "    plt.axis(\"off\")\n",
    "    plt.title(res)\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 화면에 움직임이 있는 부분 추출하기(p144)\n",
    " - 노트북으로 실행\n",
    " - cv2.absdiff() : 이미지의 차이 확인"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "error",
     "evalue": "OpenCV(3.4.2) C:\\projects\\opencv-python\\opencv\\modules\\imgproc\\src\\resize.cpp:4044: error: (-215:Assertion failed) !ssize.empty() in function 'cv::resize'\n",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31merror\u001b[0m                                     Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-2-aefaeafb03a0>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      8\u001b[0m     \u001b[1;31m# 이미지 추출하기\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      9\u001b[0m     \u001b[0m_\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mframe\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mcap\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mread\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 10\u001b[1;33m     \u001b[0mframe\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mcv2\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mresize\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mframe\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;33m(\u001b[0m\u001b[1;36m500\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m300\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     11\u001b[0m     \u001b[1;31m# 흑백 이미지로 변환하기 --- (*2)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     12\u001b[0m     \u001b[0mgray\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mcv2\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcvtColor\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mframe\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mcv2\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mCOLOR_BGR2GRAY\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31merror\u001b[0m: OpenCV(3.4.2) C:\\projects\\opencv-python\\opencv\\modules\\imgproc\\src\\resize.cpp:4044: error: (-215:Assertion failed) !ssize.empty() in function 'cv::resize'\n"
     ]
    }
   ],
   "source": [
    "import cv2\n",
    "\n",
    "cap = cv2.VideoCapture(0)\n",
    "img_last = None # 이전 프레임을 저장해둘 변수 --- (*1)\n",
    "green = (0, 255, 0)\n",
    "\n",
    "while True:\n",
    "    # 이미지 추출하기\n",
    "    _, frame = cap.read()\n",
    "    frame = cv2.resize(frame, (500, 300))\n",
    "    # 흑백 이미지로 변환하기 --- (*2)\n",
    "    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)\n",
    "    gray = cv2.GaussianBlur(gray, (9, 9), 0)\n",
    "    img_b = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)[1]\n",
    "    # 차이 확인하기\n",
    "    if img_last is None:\n",
    "        img_last = img_b\n",
    "        continue\n",
    "    frame_diff = cv2.absdiff(img_last, img_b) # --- (*3)\n",
    "    cnts = cv2.findContours(frame_diff, \n",
    "            cv2.RETR_EXTERNAL,\n",
    "            cv2.CHAIN_APPROX_SIMPLE)[1]\n",
    "    # 차이가 있는 부분 출력하기 --- (*4)\n",
    "    for pt in cnts:\n",
    "        x, y, w, h = cv2.boundingRect(pt)\n",
    "        if w < 30: continue # 작은 변경은 무시하기\n",
    "        cv2.rectangle(frame, (x, y), (x+w, y+h), green, 2)\n",
    "    # 프레임을 변수에 저장해두기 --- (*5)\n",
    "    img_last = img_b\n",
    "    # 화면에 출력하기\n",
    "    cv2.imshow(\"Diff Camera\", frame)\n",
    "    cv2.imshow(\"diff data\", frame_diff)\n",
    "    if cv2.waitKey(1) == 27: break\n",
    "cap.release()\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 동영상에서 열대어가 나오는 부분 검출하기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "FileExistsError",
     "evalue": "[WinError 183] 파일이 이미 있으므로 만들 수 없습니다: './exfish'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileExistsError\u001b[0m                           Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-2-817f91ca5be5>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[0mno\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;36m0\u001b[0m \u001b[1;31m# 이미지 장 수\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0msave_dir\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m\"./exfish\"\u001b[0m \u001b[1;31m# 저장 디렉터리 이름\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 6\u001b[1;33m \u001b[0mos\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mmkdir\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0msave_dir\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;31m# 디렉터리 만들기\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      7\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      8\u001b[0m \u001b[1;31m# 동영상 파일로부터 입력받기 --- (*1)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mFileExistsError\u001b[0m: [WinError 183] 파일이 이미 있으므로 만들 수 없습니다: './exfish'"
     ]
    }
   ],
   "source": [
    "import cv2, os\n",
    "\n",
    "img_last = None # 이전 프레임을 저장할 변수\n",
    "no = 0 # 이미지 장 수\n",
    "save_dir = \"./exfish\" # 저장 디렉터리 이름\n",
    "os.mkdir(save_dir) # 디렉터리 만들기\n",
    "\n",
    "# 동영상 파일로부터 입력받기 --- (*1)\n",
    "cap = cv2.VideoCapture(\"fish.mp4\")\n",
    "while True:\n",
    "    # 이미지 추출하기\n",
    "    is_ok, frame = cap.read()\n",
    "    if not is_ok: break\n",
    "    frame = cv2.resize(frame, (640, 360))\n",
    "    # 흑백 이미지로 변환하기 --- (*2)\n",
    "    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)\n",
    "    gray = cv2.GaussianBlur(gray, (15, 15), 0)\n",
    "    img_b = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]\n",
    "    # 차이 확인하기\n",
    "    if not img_last is None:\n",
    "        frame_diff = cv2.absdiff(img_last, img_b) # --- (*3)\n",
    "        cnts = cv2.findContours(frame_diff, \n",
    "            cv2.RETR_EXTERNAL,\n",
    "            cv2.CHAIN_APPROX_SIMPLE)[1]\n",
    "        # 차이가 있는 부분을 파일로 출력하기 --- (*4)\n",
    "        for pt in cnts:\n",
    "            x, y, w, h = cv2.boundingRect(pt)\n",
    "            if w < 100 or w > 500: continue # 노이즈 제거하기\n",
    "            # 추출한 영역 저장하기\n",
    "            imgex = frame[y:y+h, x:x+w]\n",
    "            outfile = save_dir + \"/\" + str(no) + \".jpg\"\n",
    "            cv2.imwrite(outfile, imgex)\n",
    "            no += 1\n",
    "    img_last = img_b\n",
    "cap.release()\n",
    "print(\"ok\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 학습이미지 준비하기 \n",
    " (1) 열대어가 나오는이미지와, 나오지 않는 이미지 각 fish / nofish로 150장 뽑기"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 머신러닝으로 동영상에서 열대어가 많이 나오는 부분 찾기"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\student\\Anaconda3\\lib\\site-packages\\sklearn\\externals\\joblib\\__init__.py:15: DeprecationWarning: sklearn.externals.joblib is deprecated in 0.21 and will be removed in 0.23. Please import this functionality directly from joblib, which can be installed with: pip install joblib. If this warning is raised when loading pickled models, you may need to re-serialize those models with scikit-learn 0.21+.\n",
      "  warnings.warn(msg, category=DeprecationWarning)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "C:\\Users\\student\\Desktop\\DATA\\OpenCV\\EX/nofish\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\student\\Anaconda3\\lib\\site-packages\\sklearn\\ensemble\\forest.py:245: FutureWarning: The default value of n_estimators will change from 10 in version 0.20 to 100 in 0.22.\n",
      "  \"10 in version 0.20 to 100 in 0.22.\", FutureWarning)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.9655172413793104\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "['fish.pkl']"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import cv2\n",
    "import os, glob\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn import datasets, metrics\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.metrics import accuracy_score\n",
    "from sklearn.externals import joblib\n",
    "\n",
    "# 이미지 학습 크기와 경로 지정하기\n",
    "image_size = (64, 32)\n",
    "path = os.path.dirname(os.path.abspath(\"__file__\"))\n",
    "path_fish = path + '/fish'\n",
    "path_nofish = path + '/nofish'\n",
    "print(path_nofish)\n",
    "x = [] # 이미지 데이터\n",
    "y = [] # 레이블 데이터\n",
    "\n",
    "# 이미지 데이터를 읽어 들이고 배열에 넣기 --- (*1)\n",
    "def read_dir(path, label):\n",
    "    files = glob.glob(path + \"/*.jpg\")\n",
    "    \n",
    "    for f in files:\n",
    "        img = cv2.imread(f)\n",
    "        img = cv2.resize(img, image_size)\n",
    "        img_data = img.reshape(-1, ) # 1차원으로 전개하기\n",
    "        x.append(img_data)\n",
    "        y.append(label)\n",
    "\n",
    "# 이미지 데이터 읽어 들이기\n",
    "read_dir(path_nofish, 0)\n",
    "read_dir(path_fish, 1)\n",
    "\n",
    "# 데이터를 학습 전용과 테스트 전용으로 분리하기 --- (*2)\n",
    "x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)\n",
    "\n",
    "# 데이터 학습하기 --- (*3)\n",
    "clf = RandomForestClassifier()\n",
    "clf.fit(x_train, y_train)\n",
    "\n",
    "# 정답률 확인하기 --- (*4)\n",
    "y_pred = clf.predict(x_test)\n",
    "print(accuracy_score(y_test, y_pred))\n",
    "\n",
    "# 데이터 저장하기 --- (*5)\n",
    "joblib.dump(clf, 'fish.pkl')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 동영상분석하기"
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
      "ok 58 / 1979\n"
     ]
    }
   ],
   "source": [
    "import cv2, os, copy\n",
    "from sklearn.externals import joblib\n",
    "\n",
    "# 학습한 데이터 읽어 들이기\n",
    "clf = joblib.load(\"fish.pkl\")\n",
    "output_dir = \"./bestshot\"\n",
    "img_last = None # 이전 프레임을 저장할 변수\n",
    "fish_th = 3 # 이미지로 출력할 기준이 되는 물고기 수\n",
    "count = 0\n",
    "frame_count = 0\n",
    "if not os.path.isdir(output_dir): os.mkdir(output_dir)\n",
    "\n",
    "# 동영상 파일로부터 입력받기 --- (*1)\n",
    "cap = cv2.VideoCapture(\"fish.mp4\")\n",
    "while True:\n",
    "    # 이미지 추출하기\n",
    "    is_ok, frame = cap.read()\n",
    "    if not is_ok: break\n",
    "    frame = cv2.resize(frame, (640, 360))\n",
    "    frame2 = copy.copy(frame)\n",
    "    frame_count += 1\n",
    "    # 이전 프레임과 비교를 위해 흑백으로 변환하기 --- (*2)\n",
    "    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)\n",
    "    gray = cv2.GaussianBlur(gray, (15, 15), 0)\n",
    "    img_b = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]\n",
    "    if not img_last is None:\n",
    "        # 차이 추출하기\n",
    "        frame_diff = cv2.absdiff(img_last, img_b)\n",
    "        cnts = cv2.findContours(frame_diff, \n",
    "            cv2.RETR_EXTERNAL,\n",
    "            cv2.CHAIN_APPROX_SIMPLE)[1]\n",
    "        # 차이가 있는 부분에 물고기가 있는지 확인하기\n",
    "        fish_count = 0\n",
    "        for pt in cnts:\n",
    "            x, y, w, h = cv2.boundingRect(pt)\n",
    "            if w < 100 or w > 500: continue # 노이즈 제거하기\n",
    "            # 추출한 영역에 물고기가 있는지 확인하기 --- (*3)\n",
    "            imgex = frame[y:y+h, x:x+w]\n",
    "            imagex = cv2.resize(imgex, (64, 32))\n",
    "            image_data = imagex.reshape(-1, )\n",
    "            pred_y = clf.predict([image_data]) # --- (*4)\n",
    "            if pred_y[0] == 1:\n",
    "                fish_count += 1\n",
    "                cv2.rectangle(frame2, (x, y), (x+w, y+h), (0,255,0), 2)\n",
    "        # 물고기가 많이 있는지 확인하기 --- (*5)\n",
    "        if fish_count > fish_th:\n",
    "            fname = output_dir + \"/fish\" + str(count) + \".jpg\"\n",
    "            cv2.imwrite(fname, frame)\n",
    "            count += 1\n",
    "    cv2.imshow('FISH!', frame2)\n",
    "    if cv2.waitKey(1) == 13: break\n",
    "    img_last = img_b\n",
    "cap.release()\n",
    "cv2.destroyAllWindows()\n",
    "print(\"ok\", count, \"/\", frame_count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
