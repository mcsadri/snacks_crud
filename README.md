# snacks_crud

- Lab: Class 28 - Django CRUD and Forms
- Author: Manuch Sadri

## Overview

Add full CRUD functionality to your bag of tricks by building a Django project that allows Creating, Reading, Updating and Deleting.

## Feature Tasks and Requirements

- [X] Create `snacks_crud_project` Django project
- [X] Create `snacks` app
- [ ] Create `Snack` model
- [ ] title field
  - [ ] purchaser field
  - [ ] description field
  - [ ] Register model with admin

- [ ] Create `SnackListView` that extends appropriate generic view
  - [ ] associated url path is an empty string

- [ ] Create `SnackDetailView` that extends appropriate generic view
  - [ ] associated url path is `<int:pk>/`

- [ ] Create `SnackCreateView` that extends appropriate generic view
  - [ ] associated url path is `create/`

- [ ] Create `SnackUpdateView` that extends appropriate generic view
  - [ ] associated url path is `<int:pk>/update/`

- [ ] Create `SnackDeleteView` that extends appropriate generic view
  - [ ] associated url path is `<int:pk>/delete/`

- [ ] Add urls to support all views, with appropriate names
- [ ] Add templates to support all views
- [ ] Add navigation links in appropriate locations to access all pages
- [ ] Make all necessary changes to project level files for project to run
  - [ ] In other words, make it work

## Stretch Goals

- [ ] add multiple models
- [ ] use an alternate test runner
- [ ] add more advanced fields to models, e.g. created time stamp
- [ ] add styling

## UAT

- [ ] Test all Views
- [ ] Test Model
  - [ ] string representation
  - [ ] all fields
