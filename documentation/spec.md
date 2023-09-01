# KoloTV Bot Mention Tracking Project Specification

## Table of Contents
1. [Introduction](#1-introduction)
2. [Project Overview](#2-project-overview)
3. [User Roles](#3-user-roles)
4. [Core Features](#4-core-features)
5. [Technical Stack](#5-technical-stack)
6. [Deployment and Hosting](#6-deployment-and-hosting)
7. [Authorization](#7-authorization)
8. [User Interaction](#8-user-interaction)
9. [Error Handling](#9-error-handling)
10. [Data Retention and Privacy](#10-data-retention-and-privacy)
11. [Performance Optimization](#11-performance-optimization)
12. [Version Control](#12-version-control)
13. [Deployment Instructions](#13-deployment-instructions)
14. [License and Ownership](#14-license-and-ownership)
15. [Project Closure](#15-project-closure)

## 1. Introduction
This document serves as the Software Requirements Specification (SRS) for the KoloTV Bot Mention Tracking project. The primary objective of this project is to develop a Telegram bot that tracks mentions of specific words in various Telegram chats.

## 2. Project Overview
This project involves the development of a Telegram bot to track mentions of specific words in various Telegram chats. The bot is created at the request of an Kolo.TV Internet provider to monitor mentions of the provider's company. The primary objectives are to improve customer experience and expedite responses from technical support.

## 3. User Roles
- Managers: Team members who can access and manage the bot's settings.
- Support Service: Team members who respond to detected mentions.

## 4. Core Features
- Mention Tracking:
  - The bot identifies mentions of specific words using regular expressions (regex).
  - When a mention is detected, it sends a notification to a designated technical chat.
  - Notifications include the mention text and a link to the original message.

- Statistics:
  - Managers can request statistics on mentions by sending the `/stats` command to the bot in private messages.
  - Statistics include the number of mentions for different words over specific time periods.

## 5. Technical Stack
- Programming Language: Python 3.11
- Libraries/Frameworks:
  - aiogram 3.*
  - pydantic 2.*
  - sqlalchemy 2.*
  - Official Telegram API for receiving updates and sending notifications
- Database: SQLite (sqlite3)

## 6. Deployment and Hosting
The development team independently deploys the bot to the server provided by the customer.

## 7. Authorization
Additional authorization mechanisms beyond Telegram's built-in authentication are not implemented.

## 8. User Interaction
Apart from the `/stats` command, no other user interactions are available at this time.

## 9. Error Handling
The code includes try-except blocks for error handling within the application.

## 10. Data Retention and Privacy
Data retention policies and privacy measures are in place to ensure the security and privacy of collected data, especially chat content.

## 11. Performance Optimization
The bot uses an asynchronous structure to improve performance, especially when dealing with large volumes of data.

## 12. Version Control
The bot code is stored in a private GitHub repository for version control and collaboration among developers.

## 13. Deployment Instructions
Deployment instructions are provided for the customer to set up the bot on their server.

## 14. License and Ownership
The terms of ownership and licensing of the code and the project are determined in accordance with the expectations of the customer. The development team transfers all rights related to the project to the customer.

## 15. Project Closure
The project closure process includes the handover of code, documentation, and necessary credentials or access.
