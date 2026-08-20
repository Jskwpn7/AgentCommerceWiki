---
title: "FashionPose: Text to Pose to Relight Image Generation for Personalized Fashion Visualization"
type: summary
date: 2026-08-03
source_url: https://arxiv.org/abs/2507.13311
authors:
  - Chuancheng Shi
  - Yixiang Chen
  - Burong Lei
  - Jichao Chen
tags:
  - virtual-try-on
  - fashion-visualization
  - image-generation
  - misleading-representation
  - diffusion-models
  - pose-generation
summary: |
  Introduces FashionPose, first unified text-to-pose-to-relighting generation framework for fashion e-commerce. Given natural language description, predicts 2D pose, generates high-fidelity person images via diffusion model, then applies lightweight relighting. Enables accurate pose alignment, faithful garment rendering, and flexible lighting control. Provides practical solution for personalized virtual fashion display.
concepts:
  - virtual-try-on
  - fashion-visualization
  - text-to-image
  - misleading-representation
  - diffusion-models
---

## Overview

Fashion e-commerce users expect personalized previews under diverse poses and lighting, but existing methods rely on predefined poses with limited semantic flexibility and illumination adaptability.

## Key Contributions

1. **Unified Framework**: First end-to-end text-to-pose-to-relighting generation pipeline
2. **Text-Driven Conditioning**: Replaces explicit pose annotations with natural language input
3. **Diffusion Model Generation**: High-fidelity person images with garment rendering
4. **Lightweight Relighting**: Efficient illumination control guided by text input

## Technical Approach

- **Input**: Natural language description of desired pose and lighting
- **Pose Prediction**: 2D human pose from text
- **Image Generation**: Diffusion model generates person with garment
- **Relighting**: Lightweight module applies lighting control

## Implications for Consumer Protection

- **Misleading Representation**: AI-generated fashion images may not accurately represent how garments look on actual bodies
- **Body Image Concerns**: Synthetic models may promote unrealistic body standards
- **Expectation Mismatch**: Generated images may show garments differently than real-world appearance
- **Transparency**: Consumers may not realize fashion images are AI-generated rather than photographs
- **Accuracy Standards**: Current truth-in-advertising regulations may not address AI-generated product imagery

## Citations

- Paper: [[arXiv:2507.13311]](https://arxiv.org/abs/2507.13311)
