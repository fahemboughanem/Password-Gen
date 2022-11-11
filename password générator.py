{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "66f2340f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Collecting rembg\n",
      "  Downloading rembg-2.0.25-py3-none-any.whl (12 kB)\n",
      "Collecting pymatting==1.1.8\n",
      "  Downloading PyMatting-1.1.8-py3-none-any.whl (47 kB)\n",
      "\u001b[2K     \u001b[38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m47.7/47.7 kB\u001b[0m \u001b[31m102.4 kB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m kB/s\u001b[0m eta \u001b[36m0:00:01\u001b[0m:01\u001b[0m\n",
      "\u001b[?25hCollecting click==8.1.3\n",
      "  Downloading click-8.1.3-py3-none-any.whl (96 kB)\n",
      "\u001b[2K     \u001b[38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m96.6/96.6 kB\u001b[0m \u001b[31m183.1 kB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m kB/s\u001b[0m eta \u001b[36m0:00:01\u001b[0m:01\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: aiohttp==3.8.1 in /usr/lib/python3/dist-packages (from rembg) (3.8.1)\n",
      "Collecting scikit-image==0.19.3\n",
      "  Downloading scikit_image-0.19.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (13.9 MB)\n",
      "\u001b[2K     \u001b[38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m13.9/13.9 MB\u001b[0m \u001b[31m113.4 kB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0mm eta \u001b[36m0:00:01\u001b[0m[36m0:00:04\u001b[0m\n",
      "\u001b[?25hCollecting python-multipart==0.0.5\n",
      "  Downloading python-multipart-0.0.5.tar.gz (32 kB)\n",
      "  Preparing metadata (setup.py) ... \u001b[?25ldone\n",
      "\u001b[?25hRequirement already satisfied: pillow==9.2.0 in /usr/lib/python3/dist-packages (from rembg) (9.2.0)\n",
      "Collecting filetype==1.1.0\n",
      "  Downloading filetype-1.1.0-py2.py3-none-any.whl (17 kB)\n",
      "Collecting scipy==1.7.3\n",
      "  Downloading scipy-1.7.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (39.9 MB)\n",
      "\u001b[2K     \u001b[38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m39.9/39.9 MB\u001b[0m \u001b[31m182.6 kB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0mm eta \u001b[36m0:00:01\u001b[0m[36m0:00:06\u001b[0m\n",
      "\u001b[?25hCollecting asyncer==0.0.1\n",
      "  Downloading asyncer-0.0.1-py3-none-any.whl (8.1 kB)\n",
      "Collecting uvicorn==0.18.3\n",
      "  Downloading uvicorn-0.18.3-py3-none-any.whl (57 kB)\n",
      "\u001b[2K     \u001b[38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m57.4/57.4 kB\u001b[0m \u001b[31m191.9 kB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m1m210.7 kB/s\u001b[0m eta \u001b[36m0:00:01\u001b[0m\n",
      "\u001b[?25hCollecting onnxruntime==1.12.1\n",
      "  Downloading onnxruntime-1.12.1-cp310-cp310-manylinux_2_27_x86_64.whl (4.9 MB)\n",
      "\u001b[2K     \u001b[38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m4.9/4.9 MB\u001b[0m \u001b[31m185.9 kB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0mm eta \u001b[36m0:00:01\u001b[0m[36m0:00:01\u001b[0m\n",
      "\u001b[?25hCollecting gdown==4.5.1\n",
      "  Downloading gdown-4.5.1.tar.gz (14 kB)\n",
      "  Installing build dependencies ... \u001b[?25ldone\n",
      "\u001b[?25h  Getting requirements to build wheel ... \u001b[?25ldone\n",
      "\u001b[?25h  Preparing metadata (pyproject.toml) ... \u001b[?25ldone\n",
      "\u001b[?25hCollecting watchdog==2.1.9\n",
      "  Downloading watchdog-2.1.9-py3-none-manylinux2014_x86_64.whl (78 kB)\n",
      "\u001b[2K     \u001b[38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m78.4/78.4 kB\u001b[0m \u001b[31m232.5 kB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m1m251.9 kB/s\u001b[0m eta \u001b[36m0:00:01\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: tqdm==4.64.0 in /usr/lib/python3/dist-packages (from rembg) (4.64.0)\n",
      "Collecting fastapi==0.80.0\n",
      "  Downloading fastapi-0.80.0-py3-none-any.whl (54 kB)\n",
      "\u001b[2K     \u001b[38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m54.8/54.8 kB\u001b[0m \u001b[31m158.2 kB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m kB/s\u001b[0m eta \u001b[36m0:00:01\u001b[0m:01\u001b[0m\n",
      "\u001b[?25hCollecting opencv-python-headless==4.6.0.66\n",
      "  Downloading opencv_python_headless-4.6.0.66-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (48.3 MB)\n",
      "\u001b[2K     \u001b[38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m48.3/48.3 MB\u001b[0m \u001b[31m194.9 kB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0mm eta \u001b[36m0:00:01\u001b[0m[36m0:00:07\u001b[0m\n",
      "\u001b[?25hCollecting numpy==1.21.6\n",
      "  Downloading numpy-1.21.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (15.9 MB)\n",
      "\u001b[2K     \u001b[38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m15.9/15.9 MB\u001b[0m \u001b[31m198.3 kB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0mm eta \u001b[36m0:00:01\u001b[0m[36m0:00:03\u001b[0m\n",
      "\u001b[?25hCollecting imagehash==4.2.1\n",
      "  Downloading ImageHash-4.2.1.tar.gz (812 kB)\n",
      "\u001b[2K     \u001b[38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m812.6/812.6 kB\u001b[0m \u001b[31m222.3 kB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0mm eta \u001b[36m0:00:01\u001b[0m[36m0:00:01\u001b[0m\n",
      "\u001b[?25h  Preparing metadata (setup.py) ... \u001b[?25ldone\n",
      "\u001b[?25hRequirement already satisfied: anyio<4.0.0,>=3.4.0 in /usr/lib/python3/dist-packages (from asyncer==0.0.1->rembg) (3.6.1)\n",
      "Collecting starlette==0.19.1\n",
      "  Downloading starlette-0.19.1-py3-none-any.whl (63 kB)\n",
      "\u001b[2K     \u001b[38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m63.3/63.3 kB\u001b[0m \u001b[31m169.7 kB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m1m190.8 kB/s\u001b[0m eta \u001b[36m0:00:01\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: pydantic!=1.7,!=1.7.1,!=1.7.2,!=1.7.3,!=1.8,!=1.8.1,<2.0.0,>=1.6.2 in /usr/lib/python3/dist-packages (from fastapi==0.80.0->rembg) (1.9.0)\n",
      "Requirement already satisfied: requests[socks] in /usr/lib/python3/dist-packages (from gdown==4.5.1->rembg) (2.27.1)\n",
      "Requirement already satisfied: six in /usr/lib/python3/dist-packages (from gdown==4.5.1->rembg) (1.16.0)\n",
      "Requirement already satisfied: filelock in /usr/lib/python3/dist-packages (from gdown==4.5.1->rembg) (3.8.0)\n",
      "Requirement already satisfied: beautifulsoup4 in /usr/lib/python3/dist-packages (from gdown==4.5.1->rembg) (4.11.1)\n",
      "Collecting PyWavelets\n",
      "  Downloading PyWavelets-1.4.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (6.8 MB)\n",
      "\u001b[2K     \u001b[38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.8/6.8 MB\u001b[0m \u001b[31m177.5 kB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0mm eta \u001b[36m0:00:01\u001b[0m[36m0:00:02\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: flatbuffers in /usr/lib/python3/dist-packages (from onnxruntime==1.12.1->rembg) (2.0.6+dfsg1.3)\n",
      "Requirement already satisfied: packaging in /usr/lib/python3/dist-packages (from onnxruntime==1.12.1->rembg) (21.3)\n",
      "Requirement already satisfied: protobuf in /usr/lib/python3/dist-packages (from onnxruntime==1.12.1->rembg) (3.12.4)\n",
      "Requirement already satisfied: sympy in /usr/lib/python3/dist-packages (from onnxruntime==1.12.1->rembg) (1.10.1)\n",
      "Collecting coloredlogs\n",
      "  Downloading coloredlogs-15.0.1-py2.py3-none-any.whl (46 kB)\n",
      "\u001b[2K     \u001b[38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m46.0/46.0 kB\u001b[0m \u001b[31m195.8 kB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m1m208.9 kB/s\u001b[0m eta \u001b[36m0:00:01\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: numba!=0.49.0 in /usr/lib/python3/dist-packages (from pymatting==1.1.8->rembg) (0.55.2)\n",
      "Requirement already satisfied: networkx>=2.2 in /usr/lib/python3/dist-packages (from scikit-image==0.19.3->rembg) (2.6.3)\n",
      "Collecting tifffile>=2019.7.26\n",
      "  Downloading tifffile-2022.10.10-py3-none-any.whl (210 kB)\n",
      "\u001b[2K     \u001b[38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m210.3/210.3 kB\u001b[0m \u001b[31m154.1 kB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m[36m0:00:01\u001b[0m[36m0:00:01\u001b[0m:01\u001b[0m\n",
      "\u001b[?25hCollecting imageio>=2.4.1\n",
      "  Downloading imageio-2.22.3-py3-none-any.whl (3.4 MB)\n",
      "\u001b[2K     \u001b[38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m3.4/3.4 MB\u001b[0m \u001b[31m93.7 kB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0mm eta \u001b[36m0:00:01\u001b[0m[36m0:00:01\u001b[0mm\n",
      "\u001b[?25hRequirement already satisfied: h11>=0.8 in /usr/lib/python3/dist-packages (from uvicorn==0.18.3->rembg) (0.13.0)\n",
      "Collecting humanfriendly>=9.1\n",
      "  Downloading humanfriendly-10.0-py2.py3-none-any.whl (86 kB)\n",
      "\u001b[2K     \u001b[38;2;114;156;31m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m86.8/86.8 kB\u001b[0m \u001b[31m117.1 kB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m1m126.6 kB/s\u001b[0m eta \u001b[36m0:00:01\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: PySocks!=1.5.7,>=1.5.6 in /usr/lib/python3/dist-packages (from requests[socks]->gdown==4.5.1->rembg) (1.7.1)\n",
      "Building wheels for collected packages: gdown, imagehash, python-multipart\n",
      "  Building wheel for gdown (pyproject.toml) ... \u001b[?25ldone\n",
      "\u001b[?25h  Created wheel for gdown: filename=gdown-4.5.1-py3-none-any.whl size=14933 sha256=4c0e4273c90d469561e54985fe56a9144da507887bf7b3bf18a7cd836c6fdf1a\n",
      "  Stored in directory: /home/kali/.cache/pip/wheels/73/b9/12/4bc74ed5fe80e24c009a13db76b5edf7fa550dc426094fd284\n",
      "  Building wheel for imagehash (setup.py) ... \u001b[?25ldone\n",
      "\u001b[?25h  Created wheel for imagehash: filename=ImageHash-4.2.1-py2.py3-none-any.whl size=295189 sha256=6e9f620872681a392f3062b39048635705152446b123de2378cf1846ea80230b\n",
      "  Stored in directory: /home/kali/.cache/pip/wheels/18/c3/6f/a5c2b1a012bd3ee46b93838d206260e0004a2859feb7baef26\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  Building wheel for python-multipart (setup.py) ... \u001b[?25ldone\n",
      "\u001b[?25h  Created wheel for python-multipart: filename=python_multipart-0.0.5-py3-none-any.whl size=31671 sha256=7842bd6acc9b237ab46bd7277323a5c99cd38cfe9a46b024303e0cc382b15be4\n",
      "  Stored in directory: /home/kali/.cache/pip/wheels/1a/70/03/c981b93a16009e0e54f9f16e19fd8e94c5415b805f61fd2a07\n",
      "Successfully built gdown imagehash python-multipart\n",
      "Installing collected packages: filetype, watchdog, starlette, python-multipart, numpy, humanfriendly, click, asyncer, uvicorn, tifffile, scipy, PyWavelets, opencv-python-headless, imageio, gdown, fastapi, coloredlogs, scikit-image, pymatting, onnxruntime, imagehash, rembg\n",
      "\u001b[33m  WARNING: The script filetype is installed in '/home/kali/.local/bin' which is not on PATH.\n",
      "  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.\u001b[0m\u001b[33m\n",
      "\u001b[0m\u001b[33m  WARNING: The script watchmedo is installed in '/home/kali/.local/bin' which is not on PATH.\n",
      "  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.\u001b[0m\u001b[33m\n",
      "\u001b[0m\u001b[33m  WARNING: The scripts f2py, f2py3 and f2py3.10 are installed in '/home/kali/.local/bin' which is not on PATH.\n",
      "  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.\u001b[0m\u001b[33m\n",
      "\u001b[0m\u001b[33m  WARNING: The script humanfriendly is installed in '/home/kali/.local/bin' which is not on PATH.\n",
      "  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.\u001b[0m\u001b[33m\n",
      "\u001b[0m\u001b[33m  WARNING: The script uvicorn is installed in '/home/kali/.local/bin' which is not on PATH.\n",
      "  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.\u001b[0m\u001b[33m\n",
      "\u001b[0m\u001b[33m  WARNING: The scripts lsm2bin, tiff2fsspec, tiffcomment and tifffile are installed in '/home/kali/.local/bin' which is not on PATH.\n",
      "  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.\u001b[0m\u001b[33m\n",
      "\u001b[0m\u001b[33m  WARNING: The scripts imageio_download_bin and imageio_remove_bin are installed in '/home/kali/.local/bin' which is not on PATH.\n",
      "  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.\u001b[0m\u001b[33m\n",
      "\u001b[0m\u001b[33m  WARNING: The script gdown is installed in '/home/kali/.local/bin' which is not on PATH.\n",
      "  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.\u001b[0m\u001b[33m\n",
      "\u001b[0m\u001b[33m  WARNING: The script coloredlogs is installed in '/home/kali/.local/bin' which is not on PATH.\n",
      "  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.\u001b[0m\u001b[33m\n",
      "\u001b[0m\u001b[33m  WARNING: The script skivi is installed in '/home/kali/.local/bin' which is not on PATH.\n",
      "  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.\u001b[0m\u001b[33m\n",
      "\u001b[0m\u001b[33m  WARNING: The script onnxruntime_test is installed in '/home/kali/.local/bin' which is not on PATH.\n",
      "  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.\u001b[0m\u001b[33m\n",
      "\u001b[0m\u001b[33m  WARNING: The script rembg is installed in '/home/kali/.local/bin' which is not on PATH.\n",
      "  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.\u001b[0m\u001b[33m\n",
      "\u001b[0mSuccessfully installed PyWavelets-1.4.1 asyncer-0.0.1 click-8.1.3 coloredlogs-15.0.1 fastapi-0.80.0 filetype-1.1.0 gdown-4.5.1 humanfriendly-10.0 imagehash-4.2.1 imageio-2.22.3 numpy-1.21.6 onnxruntime-1.12.1 opencv-python-headless-4.6.0.66 pymatting-1.1.8 python-multipart-0.0.5 rembg-2.0.25 scikit-image-0.19.3 scipy-1.7.3 starlette-0.19.1 tifffile-2022.10.10 uvicorn-0.18.3 watchdog-2.1.9\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install rembg\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "7f78c832",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the length of password :5\n",
      "ik@bD\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "passlen = int (input(\"enter the length of password :\"))\n",
    "s= \"absdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ!@#$%\"\n",
    "p= \"\".join(random.sample(s,passlen))\n",
    "print(p)\n",
    "#clcoding.com"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d5df3c2c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "431ab27c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9b258112",
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
