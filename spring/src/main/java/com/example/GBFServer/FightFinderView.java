package com.example.GBFServer;

import java.io.File;
import java.net.URISyntaxException;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class FightFinderView {
    
    @CrossOrigin
    @GetMapping("/fights")
    public String[] GetFights() {
        try {
            String[] list = getAllDictInRes("fights");
            return list;
        } catch (URISyntaxException e) {
            e.printStackTrace();
        }
        return null;
    }


    private String[] getAllDictInRes(String folder) throws URISyntaxException {

        ClassLoader classLoader = getClass().getClassLoader();

        File resourcePath = new File(classLoader.getResource(folder).toURI());

        return resourcePath.list((f, name) -> f.isDirectory());
    }
}
