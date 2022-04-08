package com.sanalyapp.sanaly.dao;

import com.sanalyapp.sanaly.model.User;

import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

public class FakeUserData implements UserDao{
    private static List<User> DB = new ArrayList<>();
    @Override
    public int insertUser(UUID id, User user) {
        DB.add(new User(id, user.getFirstName(), user.getLastName(), user.getEmail(), user.getPassword(), user.getPhone()));
        return 0;
    }
}
