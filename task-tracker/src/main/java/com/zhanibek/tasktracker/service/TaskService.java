package com.zhanibek.tasktracker.service;

import com.zhanibek.tasktracker.dao.TaskDao;
import com.zhanibek.tasktracker.model.Task;

public class TaskService {
    private TaskDao taskDao;

    public TaskService(TaskDao taskDao){
        this.taskDao = taskDao;
    }

    public int addTask(Task task){
        return taskDao.insertTask(task);
    }
}
