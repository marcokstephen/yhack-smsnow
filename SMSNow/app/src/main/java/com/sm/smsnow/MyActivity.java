package com.sm.smsnow;

import android.app.Activity;
import android.content.Context;
import android.os.Bundle;
import android.telephony.SmsManager;
import android.view.View;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.ListView;
import android.widget.Toast;

public class MyActivity extends Activity {

    Context ctxt;
    private static final String STORED_WEATHER = "com.sm.smsnow.STORED_WEATHER";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_my);
        ctxt = this;
        final SmsManager smsManager = SmsManager.getDefault();

        final EditText locationEditText = (EditText)findViewById(R.id.editText_location);
        ListView lv = (ListView)findViewById(R.id.listView_main);
        ImageView refreshView = (ImageView)findViewById(R.id.imageView_refresh);
        refreshView.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String location = locationEditText.getText().toString();
                String twilioNumber = ctxt.getString(R.string.twilio_number);
                smsManager.sendTextMessage(twilioNumber,null,"weather forecast in "+location,null,null);
                smsManager.sendTextMessage(twilioNumber,null,"attractions "+location,null,null);
                Toast.makeText(ctxt,"Refreshing...",Toast.LENGTH_SHORT).show();
            }
        });
    }
}
