---

description: "Task list for Python Todo App implementation"
---

# Tasks: Python Todo App

**Input**: Design documents from `/specs/001-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan in src/
- [X] T002 [P] Create src/main.py file for main application entry point
- [X] T003 [P] Create src/todo_app.py file for core TodoApp class
- [X] T004 [P] Create src/models/ directory and __init__.py file
- [X] T005 [P] Create src/utils/ directory and __init__.py file
- [X] T006 [P] Create tests/ directory with unit/ and integration/ subdirectories

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T007 Create Task model in src/models/task.py with id, title, and completed properties
- [X] T008 Create input validation utilities in src/utils/validators.py
- [X] T009 Create TodoApp class skeleton in src/todo_app.py with in-memory storage
- [X] T010 [P] Create basic menu system in src/main.py
- [X] T011 [P] Create unit test file for Task model in tests/unit/test_task.py
- [X] T012 [P] Create unit test file for TodoApp in tests/unit/test_todo_app.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks to their todo list with a title

**Independent Test**: Can successfully add a new task with a title and see it appear in the task list with a pending status.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

- [X] T013 [P] [US1] Create unit test for adding valid task in tests/unit/test_todo_app.py
- [X] T014 [P] [US1] Create unit test for adding task with empty title in tests/unit/test_todo_app.py

### Implementation for User Story 1

- [X] T015 [US1] Implement add_task method in src/todo_app.py with validation
- [X] T016 [US1] Implement add task functionality in main menu in src/main.py
- [X] T017 [US1] Update Task model to include validation for non-empty title in src/models/task.py
- [X] T018 [US1] Add error handling for empty title in src/utils/validators.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Task List (Priority: P1)

**Goal**: Allow users to view all their tasks with titles and completion status

**Independent Test**: Can display all tasks with their titles and completion status in a clear, readable format.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [X] T019 [P] [US2] Create unit test for viewing empty task list in tests/unit/test_todo_app.py
- [X] T020 [P] [US2] Create unit test for viewing populated task list in tests/unit/test_todo_app.py

### Implementation for User Story 2

- [X] T021 [US2] Implement view_tasks method in src/todo_app.py
- [X] T022 [US2] Implement view task list functionality in main menu in src/main.py
- [X] T023 [US2] Create task display formatting function in src/todo_app.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Tasks as Complete (Priority: P2)

**Goal**: Allow users to mark tasks as complete to track progress

**Independent Test**: Can mark a specific task as complete and see the status change in the task list.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [X] T024 [P] [US3] Create unit test for marking valid task as complete in tests/unit/test_todo_app.py
- [X] T025 [P] [US3] Create unit test for marking invalid task ID as complete in tests/unit/test_todo_app.py

### Implementation for User Story 3

- [X] T026 [US3] Implement mark_task_complete method in src/todo_app.py
- [X] T027 [US3] Implement mark task complete functionality in main menu in src/main.py
- [X] T028 [US3] Add error handling for invalid task ID in src/utils/validators.py

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Update Task Title (Priority: P3)

**Goal**: Allow users to update the title of existing tasks

**Independent Test**: Can update the title of a specific task and see the change reflected in the task list.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [X] T029 [P] [US4] Create unit test for updating valid task title in tests/unit/test_todo_app.py
- [X] T030 [P] [US4] Create unit test for updating with invalid task ID in tests/unit/test_todo_app.py

### Implementation for User Story 4

- [X] T031 [US4] Implement update_task method in src/todo_app.py
- [X] T032 [US4] Implement update task functionality in main menu in src/main.py
- [X] T033 [US4] Add validation for non-empty title in update operation in src/utils/validators.py

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Delete Tasks (Priority: P3)

**Goal**: Allow users to delete tasks they no longer need

**Independent Test**: Can delete a specific task and confirm it's removed from the task list.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [X] T034 [P] [US5] Create unit test for deleting valid task in tests/unit/test_todo_app.py
- [X] T035 [P] [US5] Create unit test for deleting with invalid task ID in tests/unit/test_todo_app.py

### Implementation for User Story 5

- [X] T036 [US5] Implement delete_task method in src/todo_app.py
- [X] T037 [US5] Implement delete task functionality in main menu in src/main.py
- [X] T038 [US5] Add error handling for delete operation in src/utils/validators.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T039 [P] Add comprehensive error messages for all operations in src/todo_app.py
- [X] T040 [P] Update main menu to display task list after each operation in src/main.py
- [X] T041 [P] Add integration tests for complete user workflows in tests/integration/test_end_to_end.py
- [ ] T042 [P] Documentation updates in docs/
- [X] T043 Code cleanup and refactoring
- [X] T044 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Create unit test for adding valid task in tests/unit/test_todo_app.py"
Task: "Create unit test for adding task with empty title in tests/unit/test_todo_app.py"

# Launch all implementation for User Story 1 together:
Task: "Implement add_task method in src/todo_app.py with validation"
Task: "Implement add task functionality in main menu in src/main.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence