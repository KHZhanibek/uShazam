package com.zhanibek.tasktracker.model;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.UUID;

public class Project {
    enum Status{
        NotStarted,
        Active,
        Completed
    }

    //Fields
    private List<Task> tasks;
    private UUID id;
    private String name;
    private Date startDate, endDate;
    private Status status;

    //Constructors
    public Project(UUID id, String name, Date startDate, Date endDate, Status status) {
        this.id = id;
        this.name = name;
        this.startDate = startDate;
        this.endDate = endDate;
        this.status = status;
        tasks = new ArrayList<Task>();
    }

    //Getter/Setters
    public UUID getId() {return id;}

    public void setId(UUID id) {this.id = id;}

    public String getName() {return name;}

    public void setName(String name) {this.name = name;}

    public Date getStartDate() {return startDate;}

    public void setStartDate(Date startDate) {this.startDate = startDate;}

    public Date getEndDate() {return endDate;}

    public void setEndDate(Date endDate) {this.endDate = endDate;}

    public Status getStatus() {return status;}

    public void setStatus(Status status) {this.status = status;}

    //tasks add/delete


}
