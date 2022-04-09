package com.zhanibek.tasktracker.model;

import java.util.UUID;

public class Task {
    enum Status{
        ToDo,
        InProgress,
        Done
    }

    private UUID id;
    private String name, description;
    private int priority;
    private Status status;

    public int getPriority() {return priority;}

    public void setPriority(int priority) {this.priority = priority;}

    public UUID getId() {
        return id;
    }

    public void setId(UUID id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
}
