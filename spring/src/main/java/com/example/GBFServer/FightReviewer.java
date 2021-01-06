package com.example.GBFServer;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URISyntaxException;

@RestController
public class FightReviewer {

    @CrossOrigin
    @GetMapping("/fight/{fightDirName}")
    public String fightLoader(@PathVariable String fightDirName) throws URISyntaxException {

        ClassLoader classLoader = getClass().getClassLoader();
        File resourcePath = new File(classLoader.getResource("python/gbf_battle_reader.py").toURI());
        File fightPath = new File(classLoader.getResource("fights/" + fightDirName).toURI());
        
        ProcessBuilder processBuilder = new ProcessBuilder("python3", resourcePath.toString(), fightPath.toString()+"/");
        StringBuilder sb = new StringBuilder();
        try {
            Process process = processBuilder.start();
            BufferedReader br = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            while ((line = br.readLine()) != null) {
                sb.append(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        return sb.toString();
    }
}
