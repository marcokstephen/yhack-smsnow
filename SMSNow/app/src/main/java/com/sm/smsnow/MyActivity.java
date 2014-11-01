package com.sm.smsnow;

import android.app.Activity;
import android.content.Context;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.Toast;

public class MyActivity extends Activity {

    Context ctxt;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_my);
        ctxt = this;

        ImageView refreshView = (ImageView)findViewById(R.id.imageView_refresh);
        refreshView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Toast.makeText(ctxt,"Refreshing...",Toast.LENGTH_SHORT).show();
            }
        });
    }
}
