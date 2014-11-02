package com.sm.smsnow;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.telephony.SmsMessage;
import android.widget.Toast;

public class SMSReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(Context context, Intent intent) {
        Bundle bundle = intent.getExtras();
        Object[] messages = (Object[])bundle.get("pdus");
        SmsMessage[] sms = new SmsMessage[messages.length];

        for (int i = 0; i < messages.length; i++){
            sms[i] = SmsMessage.createFromPdu((byte[])messages[i]);
        }
        for (int i = 0; i < sms.length; i++){
            SmsMessage msg = sms[i];
            String twilioNum = context.getString(R.string.twilio_number);
            if (msg.getOriginatingAddress().equals(twilioNum)){
                //act on the message, it is from twilio

                Toast.makeText(context,msg.getMessageBody(),Toast.LENGTH_SHORT).show();
            }
            //else, it is just a normal message!
        }
    }
}
