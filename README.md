# 🧭 Image Alignment using OpenCV (ORB + Homography)

Align scanned images with their original templates using feature detection and homography estimation with OpenCV.

---

## 📌 Table of Contents

- [📌 Table of Contents](#-table-of-contents)
- [📸 Demo](#-demo)
- [🚀 Features](#-features)
- [🛠 How It Works](#-how-it-works)
- [📂 Project Structure](#-project-structure)
- [📦 Requirements](#-requirements)
- [▶️ Getting Started](#️-getting-started)
- [📝 Notes](#-notes)
- [📘 License](#-license)

---

## 📸 Demo

| Original Form | Scanned Form | Aligned Output |
|---------------|--------------|----------------|
| ![Original](form.jpg) | ![Scanned](scanned-form.jpg) | 🖼️ Shown in Output Window |

---

## 🚀 Features

✅ ORB keypoint detection  
✅ BruteForce-Hamming feature matching  
✅ Top 10% best match filtering  
✅ Homography estimation with RANSAC  
✅ Image warping for alignment  
✅ Real-time side-by-side result display

---

## 🛠 How It Works

1. Load and convert images to grayscale.
2. Detect keypoints and compute descriptors using **ORB**.
3. Match features using **BruteForce-Hamming** matcher.
4. Sort matches by distance and select the top 10%.
5. Estimate a **homography matrix** using RANSAC.
6. Warp the scanned image to align it with the original.
7. Display the aligned result side-by-side.

---
