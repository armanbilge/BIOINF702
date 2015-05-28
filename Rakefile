require 'open-uri'

task 'assignment1' => 'assignment1.pdf'

task 'assignment3' => 'assignment3.pdf'

task 'assignment4' => 'assignment4.pdf'

rule '.csl' do |t|
  open(t.name, 'w') do |f|
    f << open("https://raw.githubusercontent.com/citation-style-language/styles/master/#{t.name}").read
  end
end

rule '.pdf' => '.md' do |t|
  sh "pandoc #{t.source} -o #{t.name}"
end

file 'assignment3.pdf' => ['assignment3.md', 'apa.csl'] do |t|
  sh "pandoc --filter pandoc-citeproc #{t.source} -o #{t.name}"
end

file 'assignment3-clean.md' => ['assignment3.md', 'apa.csl'] do |t|
  sh "pandoc -t markdown #{t.source} | sed -e 's/\\[[^][]*\\]//g' | sed -e 's/\\$[^][]*\\$//g' > #{t.name}"
end

task 'wc' => 'assignment3-clean.md' do |t|
  sh "#{t.name} #{t.source}"
end
