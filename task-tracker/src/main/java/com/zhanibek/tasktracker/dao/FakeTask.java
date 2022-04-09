package com.zhanibek.tasktracker.dao;

import com.zhanibek.tasktracker.model.Task;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

public class FakeTask implements TaskDao{
    private static List<Task> DB = new ArrayList<>();

    @Override
    public int insertTask(UUID id, Task task) {
        DB.add(task);
        return 1;
    }
}
