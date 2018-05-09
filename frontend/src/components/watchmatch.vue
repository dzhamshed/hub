<template>
    <div class="page-container">
        <div style="width: calc(100% - 20px); height: 70%; border: 1px solid #000; position: absolute; left: 10px; top: 10px;">
            <!--<h2>{{ title1 }}</h2>-->
            <img id="video" src="http://localhost:5000/video" width="100%" height="100%">
            <audio id="audio" src="http://localhost:5000/audio" autoplay="autoplay"></audio>
        </div>

        <div style="width: calc(100% - 20px); height: calc(30% - 20px); border: 1px solid #000; position: absolute; left: 10px; top: calc( 70% + 10px);">
            <!--<h2>{{ title3 }}</h2>-->
            <div class="row">
                <div class="six columns"  v-for="team in teams">

                    <div class="row" style="padding: 3px">

                        <div class="two columns">
                            <img width="50px" height="50px" :src="team.icon"/>
                        </div>
                        <div class="three columns" style="height: 50px; padding: 10px;">
                            {{team.name}}
                        </div>
                    </div>
                    <div v-for="player in team.players" class="row" style="padding: 3px">
                        <div class="two columns">
                            {{player.name}}
                        </div>
                        <div class="two columns">
                            {{player.number}}
                        </div>

                        <div class="one column">
                            <button  @click="setObjectToWatch(player.name)">Switch to Player!</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        </div>
</template>
<style>
    .page-container {
    }
</style>

<script>

    export default {
        name: 'Watchmatch',
        data () {
            return {
                title1: 'Match',
                title2: 'User',
                title3: 'Logs',
                videostream: null,
                marginstream: null,
                logs: [],
                teams: []
            }
        },

        sockets: {
            output_stream: function(data) {
                this.videostream = this.marginstream;
                this.marginstream = data;
            },
            output_log: function(data) {
                this.logs.unshift(data);
                //console.log(data);
            }
        },

        created() {
            this.getMatchInfo();

        },

        mounted: function() {
            navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia || navigator.oGetUserMedia;

            if (navigator.getUserMedia) {
                window.URL = window.URL || window.webkitURL;

                navigator.getUserMedia({ video: true, audio: true }, (stream) => {
                    let mediaRecorder = new MediaRecorder(stream);

                    const rec = () => {
                        mediaRecorder.start();
                        setTimeout(() => {
                            mediaRecorder.stop();
                            rec();
                        }, 1000);
                    };

                    rec();

                    const socket = this.$socket;
                    mediaRecorder.ondataavailable = function(e) {
                        const blob = new Blob([e.data], { 'type' : 'video/webm' });
                        const fileReader = new FileReader();
                        fileReader.onload = function(event) {
                            const res = event.target.result;
                            socket.emit('user_input_stream', res);//res.substring(res.indexOf(';base64,') + 8));
                        };
                        fileReader.readAsDataURL(blob)
                    }

                }, (error) => {
                    console.log(error);
                });
            }
        },

        methods: {
            getMatchInfo: function () {
                this.$socket.emit('get_match_info', data => {
                    console.log('data', data);
                    this.teams = data;
                });
            },

            setObjectToWatch: function (objectName) {
                console.log('req', objectName);
                this.$socket.emit('setObjectToWatch', objectName, res => {
                    console.log("answer", res);
                });

            }
        }

    }
</script>
